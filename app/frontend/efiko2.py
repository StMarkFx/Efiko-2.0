import streamlit as st
from datetime import datetime
import os
from components.chat_interface import ChatInterface
from components.file_upload import FileUpload
from utils.api_client import APIClient
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables and configure
load_dotenv()
API_URL = os.getenv('API_URL', 'http://localhost:8000')

# Configure page
st.set_page_config(
    page_title="Efiko - Your Study Buddy",
    page_icon="efiko.jpg",
    layout="centered",
    initial_sidebar_state="expanded"
)

def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []
    if "current_document" not in st.session_state:
        st.session_state.current_document = None
    if "vectorstore_id" not in st.session_state:
        st.session_state.vectorstore_id = None

def display_sidebar():
    """Display sidebar with file upload and settings"""
    with st.sidebar:
        st.image("efiko.jpg", width=150)
        st.markdown("### Welcome to Efiko!")
        
        # File upload section
        st.subheader("Upload Study Material")
        uploaded_file = st.file_uploader(
            "Choose a PDF, DOCX, or TXT file",
            type=["pdf", "docx", "txt"],
            help="Max file size: 15MB"
        )
        
        if uploaded_file:
            process_uploaded_file(uploaded_file)
        
        # Display current document info
        if st.session_state.current_document:
            st.info(f"Current document: {st.session_state.current_document}")

def process_uploaded_file(file):
    """Process uploaded document"""
    try:
        with st.spinner("Processing document..."):
            api_client = APIClient(base_url=API_URL)
            response = api_client.upload_document(file)
            if response.get("success"):
                st.session_state.current_document = file.name
                st.session_state.vectorstore_id = response.get("vectorstore_id")
                st.success("Document processed successfully!")
            else:
                st.error("Error processing document")
    except Exception as e:
        st.error(f"Error: {str(e)}")

def display_chat_interface():
    """Display main chat interface"""
    st.title("Chat with Efiko")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get AI response
        try:
            api_client = APIClient(base_url=API_URL)
            response = api_client.send_message(
                content=prompt,
                conversation_history=st.session_state.conversation_history,
                vectorstore_id=st.session_state.vectorstore_id
            )
            
            # Add AI response
            st.session_state.messages.append({
                "role": "assistant",
                "content": response["content"]
            })
            
            # Update conversation history
            st.session_state.conversation_history.append({
                "role": "user",
                "content": prompt
            })
            st.session_state.conversation_history.append({
                "role": "assistant",
                "content": response["content"]
            })
            
        except Exception as e:
            st.error(f"Error: {str(e)}")

def add_export_option():
    """Add option to export chat history"""
    if st.session_state.messages:
        if st.sidebar.button("Export Chat"):
            try:
                api_client = APIClient(base_url=API_URL)
                pdf_bytes = api_client.export_chat(
                    chat_id=datetime.now().strftime("%Y%m%d_%H%M%S")
                )
                st.sidebar.download_button(
                    label="Download PDF",
                    data=pdf_bytes,
                    file_name="chat_export.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.sidebar.error(f"Error exporting chat: {str(e)}")

def main():
    # Initialize session state
    initialize_session_state()
    
    # Display sidebar with file upload
    display_sidebar()
    
    # Display main chat interface
    display_chat_interface()
    
    # Add export option
    add_export_option()

if __name__ == "__main__":
    main()
