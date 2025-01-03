import streamlit as st
import os
from components.chat_interface import ChatInterface
from components.file_upload import FileUpload
from utils.api_client import APIClient

# Configure API endpoint based on environment
API_URL = os.getenv('API_URL', 'http://localhost:8000')  # Default to local backend

# If running on Streamlit Cloud and api_url is configured
if st.secrets.get('api_url'):
    API_URL = st.secrets['api_url']
else:
    st.warning("⚠️ Using local backend at http://localhost:8000. Make sure your FastAPI backend is running!")

def main():
    st.set_page_config(
        page_title="Efiko - Your Study Buddy",
        page_icon="efiko.jpg",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    # Initialize API client with correct endpoint
    api_client = APIClient(base_url=API_URL)

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
