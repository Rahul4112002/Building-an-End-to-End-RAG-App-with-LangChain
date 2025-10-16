# Step 1: Import all necessary libraries
import streamlit as st
import os
from dotenv import load_dotenv

# LangChain Google Generative AI imports
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Document loaders for different file types
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import Docx2txtLoader


# Text splitting
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Vector store
from langchain_community.vectorstores import FAISS

# Retrieval chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# Fix for Streamlit + asyncio compatibility
import asyncio
import nest_asyncio
nest_asyncio.apply()

# Step 2: Load environment variables
load_dotenv()

# Step 3: Initialize LLM and Embeddings
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Step 4: Configure Streamlit page
st.set_page_config(
    page_title="RAG App with LangChain",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 RAG Application with LangChain")
st.markdown("Upload documents and ask questions to get AI-powered answers with sources!")

# Step 5: File upload section
uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "txt", "docx"],
    help="Supported formats: PDF, TXT, DOCX"
)

# Step 6: Process uploaded file
if uploaded_file:
    with st.spinner("📄 Processing document..."):
        # Save uploaded file temporarily
        file_path = f"temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
            
        # STEP 1: Document Loading
        st.info("Step 1/4: Loading document...")
        if uploaded_file.name.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif uploaded_file.name.endswith(".docx"):
            loader = Docx2txtLoader(file_path)
        else:
            loader = TextLoader(file_path)
        
        docs = loader.load()
        
        # STEP 2: Text Splitting
        st.info("Step 2/4: Splitting text into chunks...")
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        split_docs = splitter.split_documents(docs)
        
        # STEP 3: Embeddings & Vector Store
        st.info("Step 3/4: Creating vector embeddings...")
        vector_store = FAISS.from_documents(
            documents=split_docs,
            embedding=embeddings
        )
        
        # STEP 4: Create Retriever
        st.info("Step 4/4: Setting up retriever...")
        retriever = vector_store.as_retriever(
            search_kwargs={"k": 4}
        )
        
        # Clean up temporary file
        os.remove(file_path)
        
        st.success("✅ Document processed successfully!")
        
    # Step 7: User query input
    user_query = st.text_input(
        "❓ Ask a question about your document:",
        placeholder="e.g., What is the main topic of this document?"
    )
    
    if st.button("🔍 Get Answer") and user_query:
        with st.spinner("🤔 Generating answer..."):
            prompt = ChatPromptTemplate.from_template("""
            Answer based on the context. If answer not found, say so.
            
            Context: {context}
            Question: {input}
            Answer:
            """)
            
            document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
            retrieval_chain = create_retrieval_chain(
                retriever=retriever,
                combine_docs_chain=document_chain
            )
            
            response = retrieval_chain.invoke({"input": user_query})
            
            st.subheader("📝 Answer:")
            st.write(response["answer"])
            
            st.subheader("📚 Sources:")
            for idx, doc in enumerate(response["context"], 1):
                with st.expander(f"Source {idx}"):
                    st.text(doc.page_content[:500])
        