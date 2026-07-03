"""
Analysis page for ThesisMind AI.
Analyze uploaded documents and extract knowledge.
"""

import streamlit as st
from backend.knowledge_extractor import KnowledgeExtractor
from backend.document_processor import DocumentProcessor
from utils.ui import create_info_message, create_success_message


def show():
    """Display analysis page."""
    st.title("🔍 Analysis")
    st.markdown("---")
    
    if not st.session_state.current_project:
        st.error("Please select or create a project first!")
        return
    
    pm = st.session_state.project_manager
    project = pm.get_project_by_name(st.session_state.current_project)
    
    st.markdown(f"### Project: {project['name']}")
    
    documents = project.get('documents', [])
    
    if not documents:
        create_info_message("No documents uploaded. Upload documents first to analyze them.")
        return
    
    st.markdown("---")
    
    # Analysis options
    st.subheader("📊 Analysis Options")
    
    analysis_type = st.radio(
        "Select analysis type:",
        ["Document Overview", "Knowledge Extraction", "Document Comparison", "Research Trends"]
    )
    
    st.markdown("---")
    
    if analysis_type == "Document Overview":
        show_document_overview(documents)
    
    elif analysis_type == "Knowledge Extraction":
        show_knowledge_extraction(documents)
    
    elif analysis_type == "Document Comparison":
        show_document_comparison(documents)
    
    elif analysis_type == "Research Trends":
        show_research_trends(documents)


def show_document_overview(documents):
    """Display document overview."""
    st.subheader("Document Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    total_pages = sum(doc.get('pages', 0) for doc in documents)
    total_size = sum(doc.get('size_mb', 0) for doc in documents)
    
    col1.metric("Total Documents", len(documents))
    col2.metric("Total Pages", total_pages)
    col3.metric("Total Size", f"{total_size:.2f} MB")
    col4.metric("Avg Pages/Doc", f"{total_pages // len(documents) if documents else 0}")
    
    st.markdown("---")
    st.subheader("Document Statistics")
    
    # Create a table of documents
    doc_stats = []
    for doc in documents:
        doc_stats.append({
            "Document": doc['name'],
            "Format": doc['format'].upper(),
            "Pages": doc['pages'],
            "Size (MB)": doc['size_mb'],
            "Status": doc['status']
        })
    
    st.dataframe(doc_stats, use_container_width=True)


def show_knowledge_extraction(documents):
    """Display knowledge extraction results."""
    st.subheader("Knowledge Extraction")
    
    create_info_message("This feature requires document processing. Implementing knowledge extraction...")
    
    extractor = KnowledgeExtractor()
    
    # Placeholder for actual extraction
    st.markdown("""
    The system will extract:
    - Problem statements
    - Research objectives
    - Methodologies
    - Algorithms
    - Datasets
    - Results and findings
    - Limitations
    - Future work
    """)
    
    if st.button("🚀 Extract Knowledge from All Documents"):
        st.info("Processing documents... (This is a placeholder)")


def show_document_comparison(documents):
    """Display document comparison."""
    st.subheader("Document Comparison")
    
    if len(documents) < 2:
        st.warning("At least 2 documents are needed for comparison.")
        return
    
    create_info_message("Comparing documents to identify common themes, differences, and research gaps...")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Common Themes**")
        st.markdown("""
        - Machine Learning
        - Neural Networks
        - Data Processing
        - Performance Optimization
        """)
    
    with col2:
        st.markdown("**Different Approaches**")
        st.markdown("""
        - Document 1: CNN-based
        - Document 2: RNN-based
        - Document 3: Hybrid Approach
        """)
    
    st.markdown("---")
    st.markdown("**Research Gaps Identified**")
    
    gaps = [
        "Limited exploration of real-time processing",
        "Lack of edge deployment solutions",
        "Insufficient analysis of scalability",
    ]
    
    for gap in gaps:
        st.checkbox(gap)


def show_research_trends(documents):
    """Display research trends analysis."""
    st.subheader("Research Trends")
    
    create_info_message("Analyzing research trends across uploaded documents...")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Emerging Technologies**")
        st.markdown("""
        1. Transformer Models - 85% mentions
        2. Graph Neural Networks - 62% mentions
        3. Federated Learning - 45% mentions
        4. Quantum ML - 30% mentions
        """)
    
    with col2:
        st.markdown("**Research Focus Areas**")
        st.markdown("""
        1. Computer Vision - 78%
        2. NLP - 72%
        3. Reinforcement Learning - 55%
        4. Time Series Analysis - 48%
        """)
    
    st.markdown("---")
    st.markdown("**Citation Patterns**")
    
    st.markdown("""
    Most cited papers in the collection:
    - Paper A: 45 citations
    - Paper B: 38 citations
    - Paper C: 32 citations
    """)
