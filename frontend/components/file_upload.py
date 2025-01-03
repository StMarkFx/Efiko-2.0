import streamlit as st
from datetime import datetime
from utils.api_client import APIClient

class FileUpload:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client
    
    def render(self):
        """Render the file upload component"""
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=['pdf', 'docx', 'txt'],
            help="Max file size: 15MB"
        )
        
        if uploaded_file:
            if self._validate_file(uploaded_file):
                with st.spinner("Processing document..."):
                    try:
                        response = self.api_client.upload_document(uploaded_file)
                        if response.get("success"):
                            self._update_upload_history(uploaded_file.name)
                            st.success("Document processed successfully!")
                        else:
                            st.error("Error processing document")
                    except Exception as e:
                        st.error(f"Upload failed: {str(e)}")
    
    def _validate_file(self, file):
        """Validate file size and type"""
        MAX_SIZE = 15 * 1024 * 1024  # 15MB
        if file.size > MAX_SIZE:
            st.error("File size exceeds 15MB limit")
            return False
        return True
    
    def _update_upload_history(self, filename: str):
        """Update the upload history in session state"""
        if "upload_history" not in st.session_state:
            st.session_state.upload_history = []
        
        st.session_state.upload_history.append({
            "filename": filename,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }) 