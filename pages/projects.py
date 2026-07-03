"""
Projects page for ThesisMind AI.
Manage research projects.
"""

import streamlit as st
from backend.project_manager import ProjectManager
from utils.ui import create_success_message, create_error_message, create_info_message


def show():
    """Display projects page."""
    st.title("📂 Projects")
    st.markdown("---")
    
    pm = st.session_state.project_manager
    
    # Tabs for different actions
    tab1, tab2, tab3 = st.tabs(["All Projects", "Create Project", "Project Settings"])
    
    # Tab 1: View all projects
    with tab1:
        st.subheader("Your Projects")
        
        projects = pm.list_projects()
        
        if projects:
            for project_name in projects:
                project = pm.get_project_by_name(project_name)
                
                with st.container():
                    col1, col2, col3 = st.columns([3, 1, 1])
                    
                    with col1:
                        st.markdown(f"### {project['name']}")
                        st.caption(f"Created: {project['created_at'][:10]}")
                        st.text(project.get('description', 'No description'))
                        
                        # Progress bar
                        progress = project.get('progress', 0)
                        st.progress(progress / 100)
                        st.caption(f"Progress: {progress}%")
                    
                    with col2:
                        if st.button("📝 Edit", key=f"edit_{project['id']}"):
                            st.session_state.current_project = project_name
                            st.rerun()
                    
                    with col3:
                        if st.button("🗑️ Delete", key=f"delete_{project['id']}"):
                            pm.delete_project(project['id'])
                            st.rerun()
                
                st.markdown("---")
        else:
            create_info_message("No projects yet. Create one to get started!")
    
    # Tab 2: Create new project
    with tab2:
        st.subheader("Create New Project")
        
        col1, col2 = st.columns(2)
        
        with col1:
            project_name = st.text_input(
                "Project Name",
                placeholder="e.g., AI in Healthcare"
            )
        
        with col2:
            project_type = st.selectbox(
                "Research Type",
                ["PhD Thesis", "Master's Thesis", "Research Paper", "Technical Report"]
            )
        
        description = st.text_area(
            "Project Description",
            placeholder="Briefly describe your research focus...",
            height=100
        )
        
        keywords = st.text_input(
            "Research Keywords",
            placeholder="e.g., machine learning, neural networks, deep learning"
        )
        
        if st.button("✨ Create Project", type="primary"):
            if project_name.strip():
                project_id = pm.create_project(
                    name=project_name,
                    description=description
                )
                create_success_message(f"Project '{project_name}' created successfully!")
                st.session_state.current_project = project_name
                st.rerun()
            else:
                create_error_message("Please enter a project name!")
    
    # Tab 3: Project settings
    with tab3:
        st.subheader("Project Settings")
        
        if st.session_state.current_project:
            project = pm.get_project_by_name(st.session_state.current_project)
            
            st.markdown(f"### {project['name']}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Status", project['status'])
                st.metric("Documents", len(project['documents']))
            
            with col2:
                st.metric("Created", project['created_at'][:10])
                st.metric("Progress", f"{project['progress']}%")
            
            st.markdown("---")
            
            st.subheader("Advanced Settings")
            
            # Export format selection
            st.markdown("**Output Formats**")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.checkbox("📄 DOCX", value=True)
            with col2:
                st.checkbox("📕 PDF", value=True)
            with col3:
                st.checkbox("📝 Markdown", value=False)
            with col4:
                st.checkbox("🔬 LaTeX", value=False)
        
        else:
            create_info_message("Select a project first to view settings!")
