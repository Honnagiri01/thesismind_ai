"""
Upload Documents page for ThesisMind AI.
Handle document uploads and processing.
"""

import streamlit as st
import os
from pathlib import Path
from backend.document_processor import DocumentProcessor
from utils.ui import create_success_message, create_error_message, create_info_message
from utils.config import APP_CONFIG, UPLOADS_DIR


def show():
    """Display upload documents page."""
    st.title("📤 Upload Documents")
    st.markdown("---")
    
    if not st.session_state.current_project:
        create_error_message("Please select or create a project first!")
        return
    
    pm = st.session_state.project_manager
    project = pm.get_project_by_name(st.session_state.current_project)
    
    st.markdown(f"### Project: {project['name']}")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Documents", len(project['documents']))
    col2.metric("Max Allowed", APP_CONFIG['max_documents'])
    col3.metric("Slots Available", APP_CONFIG['max_documents'] - len(project['documents']))
    
    st.markdown("---")
    
    # Upload section
    st.subheader("📁 Upload Research Documents")
    
    st.info("""
    **Supported formats:** PDF, DOCX, TXT
    
    **Guidelines:**
    - Each document should be a research paper, thesis, or technical report
    - Maximum file size: 100 MB per document
    - Maximum documents: 20
    - Supported languages: English (primarily)
    """)
    
    # Check if slots are available
    if len(project['documents']) >= APP_CONFIG['max_documents']:
        create_error_message(
            f"Maximum documents reached ({APP_CONFIG['max_documents']}). "
            "Delete some documents to upload more."
        )
        show_uploaded_documents(project)
        return
    
    # File uploader
    uploaded_files = st.file_uploader(
        "Choose documents to upload",
        type=["pdf", "docx", "txt", "doc"],
        accept_multiple_files=True,
        help="You can select multiple files at once"
    )
    
    if uploaded_files:
        st.markdown("---")
        st.subheader(f"📋 Processing {len(uploaded_files)} Document(s)")
        
        processor = DocumentProcessor()
        
        for uploaded_file in uploaded_files:
            # Check file size
            file_size_mb = uploaded_file.size / (1024 * 1024)
            if file_size_mb > APP_CONFIG['max_file_size_mb']:
                create_error_message(
                    f"File '{uploaded_file.name}' exceeds max size of "
                    f"{APP_CONFIG['max_file_size_mb']} MB"
                )
                continue
            
            # Save file temporarily
            project_upload_dir = UPLOADS_DIR / project['id']
            project_upload_dir.mkdir(parents=True, exist_ok=True)
            
            file_path = project_upload_dir / uploaded_file.name
            
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Process document
            with st.spinner(f"Processing {uploaded_file.name}..."):
                doc_info = processor.process_document(str(file_path))
            
            if doc_info:
                # Add document to project
                doc_entry = {
                    "name": uploaded_file.name,
                    "path": str(file_path),
                    "format": doc_info['format'],
                    "pages": doc_info['pages'],
                    "size_mb": round(file_size_mb, 2),
                    "status": "processed",
                }
                
                pm.add_document(project['id'], doc_entry)
                
                create_success_message(
                    f"✓ {uploaded_file.name} uploaded and processed ({doc_info['pages']} pages)"
                )
            else:
                create_error_message(f"✗ Failed to process {uploaded_file.name}")
    
    st.markdown("---")
    show_uploaded_documents(project)


def show_uploaded_documents(project):
    """Display uploaded documents for a project."""
    st.subheader("📚 Uploaded Documents")
    
    documents = project['documents']
    
    if documents:
        for idx, doc in enumerate(documents, 1):
            with st.container():
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    st.markdown(f"**{idx}. {doc['name']}**")
                    col_a, col_b, col_c = st.columns(3)
                    col_a.caption(f"📄 Type: {doc['format'].upper()}")
                    col_b.caption(f"📖 Pages: {doc['pages']}")
                    col_c.caption(f"💾 Size: {doc['size_mb']} MB")
                
                with col2:
                    if st.button("👁️ Preview", key=f"preview_{idx}"):
                        st.session_state[f"preview_{idx}"] = not st.session_state.get(f"preview_{idx}", False)
                
                with col3:
                    if st.button("🗑️ Remove", key=f"remove_{idx}"):
                        documents.pop(idx - 1)
                        pm = st.session_state.project_manager
                        pm.save_project(project['id'], project)
                        st.rerun()
                
                st.divider()
    else:
        create_info_message("No documents uploaded yet.")
