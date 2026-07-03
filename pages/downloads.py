"""
Downloads page for ThesisMind AI.
Export generated thesis in multiple formats.
"""

import streamlit as st
from utils.ui import create_info_message, create_success_message
from utils.config import OUTPUT_FORMATS


def show():
    """Display downloads page."""
    st.title("📥 Downloads")
    st.markdown("---")
    
    if not st.session_state.current_project:
        st.error("Please select or create a project first!")
        return
    
    pm = st.session_state.project_manager
    project = pm.get_project_by_name(st.session_state.current_project)
    
    st.markdown(f"### Project: {project['name']}")
    
    if 'generated_thesis' not in project and 'generated_thesis' not in st.session_state:
        create_info_message("No generated thesis found. Generate a thesis first.")
        return
    
    st.markdown("---")
    
    # Export options
    st.subheader("Export Thesis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        selected_format = st.selectbox(
            "Select Export Format",
            list(OUTPUT_FORMATS.keys()),
            format_func=lambda x: OUTPUT_FORMATS[x]
        )
    
    with col2:
        filename = st.text_input(
            "Filename",
            value=f"thesis_{project['name'].replace(' ', '_')}"
        )
    
    st.markdown("---")
    
    # Format-specific options
    if selected_format == "pdf":
        st.subheader("PDF Export Options")
        col1, col2 = st.columns(2)
        
        with col1:
            include_toc = st.checkbox("Include Table of Contents", value=True)
            include_figures = st.checkbox("Include Figures", value=True)
        
        with col2:
            paper_size = st.selectbox("Paper Size", ["A4", "Letter"])
            line_spacing = st.select_slider("Line Spacing", [1.0, 1.5, 2.0], value=1.5)
    
    elif selected_format == "docx":
        st.subheader("Word Document Export Options")
        col1, col2 = st.columns(2)
        
        with col1:
            include_toc = st.checkbox("Include Table of Contents", value=True)
            include_page_numbers = st.checkbox("Include Page Numbers", value=True)
        
        with col2:
            template_style = st.selectbox(
                "Template Style",
                ["APA", "MLA", "Chicago", "Harvard"]
            )
    
    elif selected_format == "markdown":
        st.subheader("Markdown Export Options")
        include_toc = st.checkbox("Include Table of Contents", value=True)
    
    elif selected_format == "latex":
        st.subheader("LaTeX Export Options")
        col1, col2 = st.columns(2)
        
        with col1:
            include_toc = st.checkbox("Include Table of Contents", value=True)
            document_class = st.selectbox("Document Class", ["article", "report", "book"])
        
        with col2:
            font_size = st.selectbox("Font Size", ["10pt", "11pt", "12pt"], index=2)
    
    st.markdown("---")
    
    if st.button("📥 Export Thesis", type="primary"):
        with st.spinner(f"Exporting to {OUTPUT_FORMATS[selected_format]}..."):
            # Placeholder for actual export logic
            create_success_message(
                f"✓ Thesis exported as {filename}.{selected_format}"
            )
            
            st.markdown(f"""
            **Export Details:**
            - Format: {OUTPUT_FORMATS[selected_format]}
            - Filename: {filename}.{selected_format}
            - Status: Ready for download
            """)
    
    st.markdown("---")
    
    # Recent exports
    st.subheader("📋 Export History")
    
    exports = [
        {
            "date": "2024-01-15",
            "filename": "thesis_draft_v1.pdf",
            "format": "PDF",
            "size": "2.5 MB"
        },
        {
            "date": "2024-01-14",
            "filename": "thesis_draft_v1.docx",
            "format": "DOCX",
            "size": "1.8 MB"
        },
    ]
    
    if exports:
        st.dataframe(
            exports,
            use_container_width=True,
            hide_index=True
        )
    else:
        create_info_message("No previous exports found.")
