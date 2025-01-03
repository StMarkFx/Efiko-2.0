import streamlit as st
from components.file_upload import FileUpload
from utils.api_client import APIClient

def upload_page():
    st.title("Document Upload")
    st.markdown("### Upload your study materials")
    
    # Initialize API client
    api_client = APIClient(base_url="http://localhost:8000")
    
    # Use the FileUpload component
    FileUpload(api_client=api_client)
    
    # Additional page-specific features
    with st.expander("Supported File Types"):
        st.markdown("""
        - PDF Documents (.pdf)
        - Word Documents (.docx)
        - Text Files (.txt)
        """)
    
    # Show upload history
    if "upload_history" in st.session_state:
        st.subheader("Recent Uploads")
        for doc in st.session_state.upload_history:
            st.text(f"📄 {doc['filename']} - {doc['timestamp']}")

if __name__ == "__main__":
    upload_page() 