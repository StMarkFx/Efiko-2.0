# Efiko: Your AI-Powered Study Companion

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)        
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Project Structure](#project-structure)
8. [Key Components](#key-components)
9. [Document Processing](#document-processing)
10. [Conversation Management](#conversation-management)
11. [PDF Export](#pdf-export)
12. [Security Considerations](#security-considerations)
13. [Performance Optimization](#performance-optimization)
14. [Contributing](#contributing)
15. [License](#license)
16. [Contact](#contact)

## Introduction

Efiko is an advanced AI-powered study assistant designed to enhance the learning experience for students of all ages. Developed by St. Mark Adebayo, a Data Science Fellow at 3MTT Nigeria, Efiko leverages cutting-edge AI technologies to provide personalized learning support, answer questions, and analyze study materials.

## Features

- **Intelligent Chatbot**: Engage in educational conversations with an AI tutor powered by Google's Gemini model.
- **Document Analysis**: Upload and process various document types (PDF, DOCX, TXT) for context-aware responses.
- **Adaptive Learning**: Tailors explanations based on the user's age and learning level.
- **Conversation Memory**: Maintains context across multiple interactions for coherent dialogues.
- **Session Management**: Save and load chat sessions for continued learning.
- **PDF Export**: Generate and download conversation summaries as PDF documents.
- **User-Friendly Interface**: Built with Streamlit for an intuitive and responsive user experience.

## Technologies Used

- **Google Generative AI (Gemini)**: Powers the core AI conversation capabilities.
- **LangChain**: Facilitates document processing and text splitting.
- **HuggingFace Transformers**: Provides text embedding functionality.
- **Chroma**: Vector store for efficient similarity search.
- **Streamlit**: Creates the interactive web interface.
- **PyPDF2**: Handles PDF document processing.
- **Unstructured**: Processes various document formats.
- **ReportLab**: Generates PDF exports of conversations.
- **Pillow (PIL)**: Manages image processing for the logo.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/efiko-study-companion.git
   cd efiko-study-companion
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Obtain an API key from Google's Generative AI platform.

2. Create a `.env` file in the project root directory:
   ```bash
   cp .env.example .env
   ```

3. Open the `.env` file and replace the placeholder with your actual API key:
   ```bash
   GEMINI_API_KEY=your_actual_api_key_here
   ```

4. Ensure that `.env` is listed in your `.gitignore` file to prevent it from being committed to the repository.

Note: Never share your API key publicly or commit it to version control.

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run efiko.py
   ```

2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

3. Use the sidebar to upload study documents (PDF, DOCX, or TXT files).

4. Start chatting with Efiko in the main chat interface.

5. Optionally, use the session management features to save, load, or export your conversations.

## Project Structure

```
efiko-study-companion/
│
├── efiko.py              # Main application file
├── config.py             # Configuration file (create this)
├── requirements.txt      # Project dependencies
├── efiko.jpg             # Logo image file
├── README.md             # This file
└── LICENSE               # License file
```

## Key Components

### ConversationBuffer

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

## Environment Setup

1. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file and replace `your_gemini_api_key_here` with your actual Gemini API key.

Note: Never commit your `.env` file or share your API key publicly.