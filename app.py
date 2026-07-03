#!/usr/bin/env python3
"""
ThesisMind AI - Main Streamlit Application
AI-powered Research Synthesis Platform

This is the MAIN FILE - Run with: streamlit run app.py
"""

import streamlit as st
import sys
from pathlib import Path
import traceback

# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

# Import configuration and utilities
try:
    from utils.config import APP_CONFIG, setup_logging, get_project_path
    from utils.ui import apply_custom_theme
    from backend.project_manager import ProjectManager
    
    logger = setup_logging()
    logger.info("ThesisMind AI starting...")
    
except ImportError as e:
    st.error(f"Import Error: {e}")
    st.info("Make sure all dependencies are installed: pip install -r requirements.txt")
    sys.exit(1)

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="ThesisMind AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/Honnagiri01/thesismind_ai',
        'Report a bug': 'https://github.com/Honnagiri01/thesismind_ai/issues',
        'About': f"ThesisMind AI v{APP_CONFIG['version']} - AI-powered Research Synthesis Platform"
    }
)

# Apply custom theme
apply_custom_theme()

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if "project_manager" not in st.session_state:
    st.session_state.project_manager = ProjectManager()
    logger.info("Project manager initialized")

if "current_project" not in st.session_state:
    st.session_state.current_project = None
    
if "generated_thesis" not in st.session_state:
    st.session_state.generated_thesis = None

if "selected_opportunity" not in st.session_state:
    st.session_state.selected_opportunity = None

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================

with st.sidebar:
    st.title("🧠 ThesisMind AI")
    st.markdown("---")
    
    # Navigation
    selected_page = st.radio(
        "📍 Navigate to:",
        [
            "Dashboard",
            "Projects",
            "Upload Documents",
            "Analysis",
            "Research Gap",
            "Generate Thesis",
            "Downloads",
            "Settings",
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Project Selector
    st.subheader("📂 Project")
    
    pm = st.session_state.project_manager
    projects = pm.list_projects()
    
    if projects:
        selected_project = st.selectbox(
            "Select Active Project:",
            projects,
            key="project_selector",
            label_visibility="collapsed"
        )
        st.session_state.current_project = selected_project
    else:
        st.info("👉 Create a project to get started")
        st.session_state.current_project = None
    
    st.markdown("---")
    
    # Sidebar Info
    st.subheader("ℹ️ Info")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Version", APP_CONFIG['version'])
    with col2:
        st.metric("Status", "✅ Running")
    
    st.markdown("---")
    st.caption("Built with Streamlit & LLM")

# ============================================================================
# PAGE ROUTING
# ============================================================================

def load_page(page_name):
    """
    Dynamically load and display the selected page.
    
    Args:
        page_name: Name of the page to load
    """
    try:
        if page_name == "Dashboard":
            from pages import dashboard
            dashboard.show()
        
        elif page_name == "Projects":
            from pages import projects
            projects.show()
        
        elif page_name == "Upload Documents":
            from pages import upload_documents
            upload_documents.show()
        
        elif page_name == "Analysis":
            from pages import analysis
            analysis.show()
        
        elif page_name == "Research Gap":
            from pages import research_gap
            research_gap.show()
        
        elif page_name == "Generate Thesis":
            from pages import generate_thesis
            generate_thesis.show()
        
        elif page_name == "Downloads":
            from pages import downloads
            downloads.show()
        
        elif page_name == "Settings":
            from pages import settings
            settings.show()
        
        logger.info(f"Page loaded: {page_name}")
        
    except Exception as e:
        st.error(f"❌ Error loading page: {page_name}")
        st.error(f"Details: {str(e)}")
        logger.error(f"Error loading page {page_name}: {traceback.format_exc()}")

# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """
    Main application entry point.
    """
    try:
        # Load the selected page
        load_page(selected_page)
        
    except Exception as e:
        st.error("❌ An unexpected error occurred!")
        st.error(str(e))
        logger.error(f"Unexpected error: {traceback.format_exc()}")
        
        # Show help
        with st.expander("🔧 Troubleshooting"):
            st.markdown("""
            **Common Issues:**
            
            1. **Import Error**: Install dependencies
               ```bash
               pip install -r requirements.txt
               ```
            
            2. **Ollama Connection Error**: Start Ollama
               ```bash
               ollama serve
               ```
            
            3. **Module Not Found**: Make sure you're in the right directory
               ```bash
               pwd  # Should show: .../thesismind_ai
               ```
            
            4. **Cache Issues**: Clear Streamlit cache
               ```bash
               rm -rf ~/.streamlit/cache*
               ```
            """)

# ============================================================================
# RUN APPLICATION
# ============================================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
    except Exception as e:
        logger.critical(f"Critical error: {e}")
        st.error("Critical error occurred. Check logs for details.")
