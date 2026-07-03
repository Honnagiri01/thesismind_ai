"""
Generate Thesis page for ThesisMind AI.
Generate complete research thesis from documents.
"""

import streamlit as st
from backend.llm_interface import LLMInterface
from utils.ui import create_info_message, create_success_message
from utils.config import THESIS_STRUCTURE


def show():
    """Display generate thesis page."""
    st.title("✍️ Generate Thesis")
    st.markdown("---")
    
    if not st.session_state.current_project:
        st.error("Please select or create a project first!")
        return
    
    pm = st.session_state.project_manager
    project = pm.get_project_by_name(st.session_state.current_project)
    
    st.markdown(f"### Project: {project['name']}")
    
    documents = project.get('documents', [])
    
    if not documents:
        st.error("Please upload documents first before generating a thesis.")
        return
    
    st.markdown("---")
    
    # Initialize LLM
    llm = LLMInterface()
    
    # Thesis generation workflow
    tab1, tab2, tab3 = st.tabs(["Configuration", "Generation", "Review"])
    
    # Tab 1: Configuration
    with tab1:
        st.subheader("Thesis Configuration")
        
        col1, col2 = st.columns(2)
        
        with col1:
            thesis_title = st.text_input(
                "Thesis Title",
                value=f"Research on {project['name']}"
            )
            
            thesis_type = st.selectbox(
                "Thesis Type",
                ["PhD Thesis", "Master's Thesis", "Research Paper", "Technical Report"]
            )
        
        with col2:
            keywords = st.text_input(
                "Keywords",
                placeholder="machine learning, neural networks"
            )
            
            target_length = st.slider(
                "Target Length (pages)",
                min_value=20,
                max_value=200,
                value=100
            )
        
        st.markdown("---")
        st.subheader("Thesis Structure")
        
        # Select chapters to include
        st.info("Select which chapters to include in your thesis:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Standard Chapters:**")
            include_abstract = st.checkbox("1. Abstract", value=True)
            include_intro = st.checkbox("2. Introduction", value=True)
            include_literature = st.checkbox("3. Literature Survey", value=True)
            include_problem = st.checkbox("4. Problem Statement", value=True)
            include_gap = st.checkbox("5. Research Gap", value=True)
            include_objectives = st.checkbox("6. Objectives", value=True)
        
        with col2:
            st.markdown("**Technical Chapters:**")
            include_methodology = st.checkbox("7. Proposed Methodology", value=True)
            include_architecture = st.checkbox("8. System Architecture", value=True)
            include_algorithms = st.checkbox("9. Algorithms", value=True)
            include_implementation = st.checkbox("10. Implementation", value=True)
            include_results = st.checkbox("11. Results", value=True)
            include_evaluation = st.checkbox("12. Evaluation", value=True)
        
        st.markdown("---")
        st.subheader("Advanced Options")
        
        col1, col2 = st.columns(2)
        
        with col1:
            temperature = st.slider(
                "Creativity (Temperature)",
                min_value=0.0,
                max_value=1.0,
                value=0.7,
                help="Lower = more focused, Higher = more creative"
            )
        
        with col2:
            include_figures = st.checkbox("Generate Figures/Diagrams", value=True)
            include_references = st.checkbox("Include Reference List", value=True)
    
    # Tab 2: Generation
    with tab2:
        st.subheader("Thesis Generation")
        
        if st.button("🚀 Start Generation", type="primary"):
            # Show progress
            progress_placeholder = st.empty()
            status_placeholder = st.empty()
            
            chapters_to_generate = []
            if include_abstract:
                chapters_to_generate.append("Abstract")
            if include_intro:
                chapters_to_generate.append("Introduction")
            if include_literature:
                chapters_to_generate.append("Literature Survey")
            if include_problem:
                chapters_to_generate.append("Problem Statement")
            if include_gap:
                chapters_to_generate.append("Research Gap")
            if include_objectives:
                chapters_to_generate.append("Objectives")
            if include_methodology:
                chapters_to_generate.append("Proposed Methodology")
            if include_architecture:
                chapters_to_generate.append("System Architecture")
            if include_algorithms:
                chapters_to_generate.append("Algorithms")
            if include_implementation:
                chapters_to_generate.append("Implementation")
            if include_results:
                chapters_to_generate.append("Results")
            if include_evaluation:
                chapters_to_generate.append("Evaluation")
            
            total_chapters = len(chapters_to_generate)
            
            generated_content = {}
            
            for idx, chapter in enumerate(chapters_to_generate):
                progress = (idx + 1) / total_chapters
                progress_placeholder.progress(progress)
                status_placeholder.info(f"Generating: {chapter}...")
                
                # Generate chapter using LLM
                chapter_content = llm.generate_chapter(
                    chapter,
                    context=f"Research on {project['name']} using {len(documents)} documents"
                )
                
                generated_content[chapter] = chapter_content
            
            # Store generated thesis
            project['generated_thesis'] = {
                'title': thesis_title,
                'chapters': generated_content,
                'status': 'generated'
            }
            pm.save_project(project['id'], project)
            
            st.session_state.generated_thesis = generated_content
            
            progress_placeholder.empty()
            status_placeholder.empty()
            
            create_success_message("✓ Thesis generated successfully!")
    
    # Tab 3: Review
    with tab3:
        st.subheader("Review Generated Thesis")
        
        if 'generated_thesis' in st.session_state:
            content = st.session_state.generated_thesis
            
            # Chapter selector
            selected_chapter = st.selectbox(
                "Select Chapter to Review",
                list(content.keys())
            )
            
            if selected_chapter:
                st.markdown(f"## {selected_chapter}")
                st.markdown(content[selected_chapter])
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("✏️ Edit Chapter"):
                        st.info("Edit mode would be enabled here")
                
                with col2:
                    if st.button("🔄 Regenerate Chapter"):
                        st.info("Regenerating chapter...")
        else:
            create_info_message("Generate a thesis first to review it here.")
