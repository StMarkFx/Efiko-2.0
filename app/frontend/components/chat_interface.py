import streamlit as st
from datetime import datetime
from utils.api_client import APIClient

class ChatInterface:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client
        self.initialize_session_state()
        self.render()

    def initialize_session_state(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def render(self):
        st.title("Chat with Efiko")

        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(f"{message['content']}")

        # Chat input
        if prompt := st.chat_input("Ask me anything..."):
            # Add user message to chat
            st.session_state.messages.append({
                "role": "user",
                "content": prompt,
                "timestamp": datetime.now().isoformat()
            })

            # Get AI response
            response = self.api_client.send_message(prompt)
            
            # Add AI response to chat
            st.session_state.messages.append({
                "role": "assistant",
                "content": response.content,
                "timestamp": response.timestamp
            })
