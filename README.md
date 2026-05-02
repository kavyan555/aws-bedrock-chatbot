Project Title

LLaMA 3 Chatbot using AWS Bedrock
________________________________________
Description

This project is a web-based chatbot application that uses AWS Bedrock to access Meta’s LLaMA 3 model for generating responses. The application allows users to interact with the model in real time through a simple interface built using Streamlit.
It includes session-based chat history and a built-in mechanism to control API usage and cost.
________________________________________
Features

•	Real-time chatbot interaction

•	Integration with AWS Bedrock (LLaMA 3)

•	Secure AWS credential input

•	Session-based chat history

•	Cost control via message limit

•	Lightweight and responsive UI
________________________________________
Tech Stack

•	Python

•	Streamlit

•	AWS Bedrock

•	boto3
________________________________________
Project Structure

BEDROCK-LLAMA3-CHATBOT/

│── app.py

│── requirements.txt

│── .env

│── .gitignore

│── venv/
________________________________________
Prerequisites

•	Python 3.8 or above

•	AWS account with Bedrock access enabled

•	AWS Access Key and Secret Key
________________________________________
Installation

Install dependencies:

pip install -r requirements.txt
________________________________________
Configuration

You can either enter credentials in the UI or store them in a .env file:

AWS_ACCESS_KEY_ID=your_access_key

AWS_SECRET_ACCESS_KEY=your_secret_key
________________________________________
Running the Application

streamlit run app.py

Open the browser and navigate to:

http://localhost:8501
________________________________________
Usage

1.	Enter AWS credentials in the sidebar

2.	Click “Connect” to initialize Bedrock client

3.	Enter a message in the input field

4.	View the chatbot response

5.	Continue conversation 
