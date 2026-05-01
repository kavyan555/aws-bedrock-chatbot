import streamlit as st
import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Page config
st.set_page_config(page_title="LLaMA 3 Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 LLaMA 3 Chatbot")
st.caption("Powered by AWS Bedrock (Cost Optimized)")

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "bedrock_client" not in st.session_state:
    st.session_state.bedrock_client = None

if "message_count" not in st.session_state:
    st.session_state.message_count = 0


# Sidebar
with st.sidebar:
    st.header("⚙ AWS Configuration")

    aws_access_key = st.text_input(
        "AWS Access Key ID",
        value=os.getenv("AWS_ACCESS_KEY_ID", ""),
        type="password"
    )

    aws_secret_key = st.text_input(
        "AWS Secret Access Key",
        value=os.getenv("AWS_SECRET_ACCESS_KEY", ""),
        type="password"
    )

    region = st.selectbox("AWS Region", ["us-east-1"])

    connect = st.button("🚀 Connect")


# Connect
if connect:
    try:
        session = boto3.Session(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region
        )
        st.session_state.bedrock_client = session.client("bedrock-runtime")
        st.sidebar.success("✅ Connected")
    except Exception as e:
        st.sidebar.error(f"❌ {e}")


# Chat UI
if st.session_state.bedrock_client:

    # 🚨 HARD LIMIT (₹10 protection)
    if st.session_state.message_count >= 25:
        st.warning("🚫 Demo limit reached (cost protection enabled)")
        st.stop()

    col1, col2 = st.columns([8, 1])

    with col1:
        user_input = st.text_input("Message", placeholder="Type...", label_visibility="collapsed")

    with col2:
        send = st.button("Send")

    if send and user_input.strip():

        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })

        # ✅ FIXED PROMPT (ONLY CURRENT INPUT)
        prompt = f"<|user|>\n{user_input}\n<|assistant|>\n"

        body = {
            "prompt": prompt,
            "temperature": 0.5,
            "top_p": 0.8,
            "max_gen_len": 300
        }

        try:
            response = st.session_state.bedrock_client.invoke_model(
                modelId="meta.llama3-8b-instruct-v1:0",
                body=json.dumps(body),
                contentType="application/json",
                accept="application/json"
            )

            response_body = json.loads(response["body"].read())

            output_text = response_body.get("generation", "No response")

            # Clean output
            if "Assistant:" in output_text:
                output_text = output_text.split("Assistant:")[-1].strip()

            if "<|assistant|>" in output_text:
                output_text = output_text.split("<|assistant|>")[-1].strip()

            st.session_state.chat_history.append({
                "role": "assistant",
                "content": output_text
            })

            # count messages
            st.session_state.message_count += 1

        except Exception as e:
            st.error(f"❌ {e}")

    st.markdown("---")

    for turn in st.session_state.chat_history:
        if turn["role"] == "user":
            st.markdown(f"🧑 **You:** {turn['content']}")
        else:
            st.markdown(f"🤖 **Bot:** {turn['content']}")

else:
    st.info("Enter AWS credentials and connect 🚀")