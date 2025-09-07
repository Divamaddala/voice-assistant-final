import streamlit as st
from openai import OpenAI
import os

# Load OpenAI client (make sure OPENAI_API_KEY is set in Streamlit secrets)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("GPT-Based Smart Assistant 🤖")

# Input box for user message
user_input = st.text_input("Ask me something:")

# Send button
if st.button("Send"):
    if user_input:
        try:
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=150
            )
            response = completion.choices[0].message.content
            st.success(response)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please type a message first.")

