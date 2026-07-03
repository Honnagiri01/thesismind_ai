"""
UI Components and Styling for ThesisMind AI.
"""

import streamlit as st
from typing import Any

# ============================================================================
# CUSTOM THEME
# ============================================================================

def apply_custom_theme():
    """
    Apply custom theme to Streamlit application.
    """
    st.markdown("""
    <style>
    /* Custom colors */
    :root {
        --primary-color: #1f77b4;
        --background-color: #ffffff;
        --secondary-background-color: #f0f2f6;
        --text-color: #262730;
    }
    
    /* Streamlit customization */
    .main {
        background-color: var(--background-color);
    }
    
    .sidebar .sidebar-content {
        background-color: var(--secondary-background-color);
    }
    
    /* Button styling */
    .stButton > button {
        background-color: var(--primary-color);
        color: white;
        border-radius: 5px;
        border: none;
        padding: 8px 16px;
    }
    
    .stButton > button:hover {
        background-color: #1557a0;
    }
    
    /* Metric styling */
    .metric-card {
        background-color: var(--secondary-background-color);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# UI COMPONENTS
# ============================================================================

def create_metric_card(container, title: str, value: str, delta: str = None, delta_type: str = "neutral"):
    """
    Create a metric card.
    
    Args:
        container: Streamlit container
        title: Metric title
        value: Metric value
        delta: Delta value (optional)
        delta_type: Type of delta ("neutral", "positive", "negative")
    """
    with container:
        st.metric(label=title, value=value, delta=delta)

def create_info_message(message: str):
    """
    Display an info message.
    
    Args:
        message: Message text
    """
    st.info(f"ℹ️ {message}")

def create_success_message(message: str):
    """
    Display a success message.
    
    Args:
        message: Message text
    """
    st.success(f"✓ {message}")

def create_error_message(message: str):
    """
    Display an error message.
    
    Args:
        message: Message text
    """
    st.error(f"✗ {message}")

def create_warning_message(message: str):
    """
    Display a warning message.
    
    Args:
        message: Message text
    """
    st.warning(f"⚠️ {message}")

# ============================================================================
# FORMATTING FUNCTIONS
# ============================================================================

def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human-readable format.
    
    Args:
        size_bytes: Size in bytes
    
    Returns:
        str: Formatted size
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

def format_date(date_str: str) -> str:
    """
    Format date string.
    
    Args:
        date_str: Date string
    
    Returns:
        str: Formatted date
    """
    if date_str:
        return date_str[:10]  # YYYY-MM-DD
    return "Unknown"

# ============================================================================
# LAYOUT COMPONENTS
# ============================================================================

def create_header(title: str, subtitle: str = None, icon: str = None):
    """
    Create a header section.
    
    Args:
        title: Header title
        subtitle: Subtitle (optional)
        icon: Icon emoji (optional)
    """
    if icon:
        st.title(f"{icon} {title}")
    else:
        st.title(title)
    
    if subtitle:
        st.markdown(f"*{subtitle}*")
    
    st.markdown("---")

def create_section(title: str, icon: str = None):
    """
    Create a section header.
    
    Args:
        title: Section title
        icon: Icon emoji (optional)
    """
    if icon:
        st.subheader(f"{icon} {title}")
    else:
        st.subheader(title)

# ============================================================================
# FORM COMPONENTS
# ============================================================================

def create_project_form() -> dict:
    """
    Create a project form.
    
    Returns:
        dict: Form data
    """
    with st.form("project_form"):
        name = st.text_input("Project Name", placeholder="e.g., AI Research")
        description = st.text_area("Description", height=100)
        keywords = st.text_input("Keywords", placeholder="machine learning, AI")
        submitted = st.form_submit_button("Create Project")
        
        if submitted and name:
            return {
                "name": name,
                "description": description,
                "keywords": keywords,
                "submitted": True
            }
    
    return {"submitted": False}
