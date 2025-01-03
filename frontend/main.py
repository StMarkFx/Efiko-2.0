import streamlit as st
from components.chat_interface import ChatInterface
from components.file_upload import FileUpload
from utils.api_client import APIClient

def main():
    st.set_page_config(
        page_title="Efiko - Your Study Buddy",
        page_icon="efiko.jpg",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    # Initialize API client
    api_client = APIClient(base_url="http://localhost:8000")

    # Sidebar
    with st.sidebar:
        st.image("efiko.jpg", width=150)
        st.markdown("### Welcome to Efiko!")
        
        # File upload component
        FileUpload(api_client=api_client)

    # Main chat interface
    ChatInterface(api_client=api_client)

if __name__ == "__main__":
    main()
