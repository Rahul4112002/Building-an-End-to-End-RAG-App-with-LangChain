# 🤖 RAG Application with LangChain

A document question-answering system using Retrieval-Augmented Generation (RAG) with Google Gemini AI, LangChain, and FAISS vector store.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.3.27-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This RAG (Retrieval-Augmented Generation) application enables users to upload documents and ask questions about their content. The system intelligently retrieves relevant context from documents and generates accurate answers with source citations using advanced AI techniques.

## ✨ Features

- 📄 **Multi-Format Support**: Upload PDF, TXT, or DOCX files
- 🤖 **Google Gemini AI Integration**: Powered by Gemini 2.5 Flash for chat and Gemini Embedding-001 for embeddings
- 🔍 **Intelligent Retrieval**: Uses FAISS vector store for efficient similarity search
- 💬 **Interactive Q&A**: Ask questions and get contextual answers
- 📚 **Source Citations**: View the exact document sections used to generate answers
- 🎨 **User-Friendly Interface**: Built with Streamlit for ease of use
- ⚡ **Fast Processing**: Efficient document chunking and embedding generation

## 🛠️ Tech Stack

- **Framework**: [LangChain](https://python.langchain.com/)
- **LLM**: Google Gemini 2.5 Flash
- **Embeddings**: Google Gemini Embedding-001
- **Vector Store**: [FAISS](https://github.com/facebookresearch/faiss)
- **UI**: [Streamlit](https://streamlit.io/)
- **Document Loaders**: PyPDF, Docx2txt, TextLoader
- **Python Version**: 3.10+

## 🏗️ Architecture

```
┌─────────────────┐
│  Upload Document│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Load Document  │ ◄── PyPDF/Docx2txt/TextLoader
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Split Chunks   │ ◄── RecursiveCharacterTextSplitter
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Create Embeddings│ ◄── Google Gemini Embeddings
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Store in FAISS  │ ◄── Vector Database
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  User Query     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Retrieve Context│ ◄── Similarity Search
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Generate Answer │ ◄── Google Gemini LLM
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Display Result  │ ◄── Answer + Sources
└─────────────────┘
```

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- Google API Key for Gemini AI

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "3. Building an End-to-End RAG App with LangChain"
   ```

2. **Create virtual environment**
   ```bash
   python -m venv myenv
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   myenv\Scripts\activate

   # macOS/Linux
   source myenv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

   > **Note**: Get your Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## 🚀 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the web interface**
   
   Open your browser and navigate to `http://localhost:8501`

3. **Upload a document**
   - Click on "Browse files" or drag and drop
   - Supported formats: PDF, TXT, DOCX

4. **Ask questions**
   - Type your question in the input box
   - Click "Get Answer"
   - View the AI-generated answer and source citations

## 📁 Project Structure

```
3. Building an End-to-End RAG App with LangChain/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in repo)
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
│
├── myenv/                 # Virtual environment (not in repo)
│
└── temp_*                 # Temporary uploaded files (auto-deleted)
```

## 🔧 How It Works

### 1. **Document Loading**
The application accepts PDF, TXT, or DOCX files and loads them using appropriate LangChain document loaders.

### 2. **Text Splitting**
Documents are split into manageable chunks (500 characters with 50 character overlap) using `RecursiveCharacterTextSplitter` for better retrieval accuracy.

### 3. **Embedding Generation**
Each text chunk is converted into vector embeddings using Google's Gemini Embedding-001 model.

### 4. **Vector Storage**
Embeddings are stored in a FAISS vector database for fast similarity search.

### 5. **Query Processing**
When a user asks a question:
- The query is embedded using the same model
- FAISS retrieves the top 4 most relevant chunks
- These chunks provide context to the LLM

### 6. **Answer Generation**
Google Gemini 2.5 Flash generates an answer based on the retrieved context, ensuring accuracy and relevance.

## 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google Gemini API key | Yes |

## 📊 Key Parameters

- **Chunk Size**: 500 characters
- **Chunk Overlap**: 50 characters
- **Retrieval Count**: Top 4 relevant chunks
- **LLM Model**: Gemini 2.5 Flash
- **Embedding Model**: Gemini Embedding-001

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [LangChain](https://python.langchain.com/) for the RAG framework
- [Google](https://ai.google.dev/) for Gemini AI models
- [Streamlit](https://streamlit.io/) for the web interface
- [FAISS](https://github.com/facebookresearch/faiss) for vector similarity search

## 📧 Contact

For questions or support, please open an issue in the repository.

---

**Made with ❤️ using LangChain and Google Gemini AI**
