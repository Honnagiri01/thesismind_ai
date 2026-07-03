"""
Dashboard page for ThesisMind AI.
Displays application overview and statistics.
"""

import streamlit as st
from utils.ui import create_metric_card, create_info_message


def show():
    """Display dashboard page."""
    st.title("📊 Dashboard")
    st.markdown("---")
    
    # Overview section
    st.subheader("Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    create_metric_card(col1, "Active Projects", "0", delta="No projects yet")
    create_metric_card(col2, "Documents Uploaded", "0", delta="Ready to upload")
    create_metric_card(col3, "Theses Generated", "0", delta="Start a new project")
    create_metric_card(col4, "Total Pages Processed", "0", delta="No data yet")
    
    st.markdown("---")
    
    # Quick start section
    st.subheader("🚀 Quick Start")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Get Started in 3 Steps:
        
        1. **Create a Project**
           - Navigate to Projects page
           - Create a new research project
           - Set your research focus
        
        2. **Upload Documents**
           - Upload research papers (PDF, DOCX, TXT)
           - Support up to 20 documents
           - Each document up to 100 MB
        
        3. **Generate Thesis**
           - Review document analysis
           - Set thesis parameters
           - Generate your original thesis
        """)
    
    with col2:
        st.markdown("""
        ### Features Available:
        
        ✨ **Multi-Document Analysis**
        - Upload and analyze multiple documents
        - Automatic knowledge extraction
        - Document comparison
        
        🧠 **AI-Powered Synthesis**
        - LLM-based content generation
        - Original thesis creation
        - Academic writing quality
        
        📥 **Multiple Export Formats**
        - DOCX (Word)
        - PDF
        - Markdown
        - LaTeX
        """)
    
    st.markdown("---")
    
    # Recent activity
    st.subheader("📈 Recent Activity")
    
    create_info_message("No recent activity. Start by creating a new project!")
    
    st.markdown("---")
    
    # System information
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("System Status")
        st.markdown("""
        - **Application**: ThesisMind AI v0.1.0
        - **Status**: ✅ Running
        - **LLM Model**: Ready to configure
        - **Storage**: Available
        """)
    
    with col2:
        st.subheader("Documentation")
        st.markdown("""
        - 📖 [User Guide](https://github.com/Honnagiri01/thesismind_ai)
        - 🛠️ [Installation Guide](https://github.com/Honnagiri01/thesismind_ai)
        - 🤝 [Contributing](https://github.com/Honnagiri01/thesismind_ai)
        - 📧 [Support](https://github.com/Honnagiri01/thesismind_ai/issues)
        """)
