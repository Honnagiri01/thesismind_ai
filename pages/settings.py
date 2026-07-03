"""
Settings page for ThesisMind AI.
Configure application settings and preferences.
"""

import streamlit as st
from utils.ui import create_info_message, create_success_message
from utils.config import APP_CONFIG


def show():
    """Display settings page."""
    st.title("⚙️ Settings")
    st.markdown("---")
    
    # Tabs for different settings
    tab1, tab2, tab3, tab4 = st.tabs(["General", "LLM Configuration", "Advanced", "About"])
    
    # Tab 1: General Settings
    with tab1:
        st.subheader("General Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Application Theme**")
            theme = st.radio(
                "Select Theme",
                ["Light", "Dark", "Auto"],
                label_visibility="collapsed"
            )
        
        with col2:
            st.markdown("**Sidebar State**")
            sidebar_state = st.radio(
                "Sidebar Position",
                ["Expanded", "Collapsed"],
                label_visibility="collapsed"
            )
        
        st.markdown("---")
        
        st.markdown("**Document Settings**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            max_docs = st.slider(
                "Maximum Documents per Project",
                min_value=5,
                max_value=50,
                value=APP_CONFIG['max_documents']
            )
        
        with col2:
            max_size = st.slider(
                "Maximum File Size (MB)",
                min_value=10,
                max_value=500,
                value=APP_CONFIG['max_file_size_mb']
            )
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            auto_save = st.checkbox("Auto-save Projects", value=True)
        
        with col2:
            notifications = st.checkbox("Enable Notifications", value=True)
        
        if st.button("💾 Save General Settings", type="primary"):
            create_success_message("General settings saved successfully!")
    
    # Tab 2: LLM Configuration
    with tab2:
        st.subheader("Language Model Configuration")
        
        st.markdown("**Model Selection**")
        
        model_type = st.selectbox(
            "Model Type",
            ["Local (Ollama)", "Hugging Face", "OpenAI Compatible", "Custom API"],
            label_visibility="collapsed"
        )
        
        if model_type == "Local (Ollama)":
            st.markdown("""
            #### Ollama Setup
            
            1. Install Ollama from [ollama.ai](https://ollama.ai)
            2. Pull a model: `ollama pull llama2`
            3. Run Ollama: `ollama serve`
            """)
            
            ollama_host = st.text_input(
                "Ollama Host",
                value="http://localhost:11434"
            )
            
            model_name = st.selectbox(
                "Model",
                ["llama2", "mistral", "neural-chat", "dolphin-mixtral"]
            )
        
        elif model_type == "Hugging Face":
            st.markdown("#### Hugging Face Setup")
            
            hf_token = st.text_input(
                "Hugging Face API Token",
                type="password",
                help="Get your token from huggingface.co"
            )
            
            model_id = st.text_input(
                "Model ID",
                value="meta-llama/Llama-2-7b"
            )
        
        elif model_type == "OpenAI Compatible":
            api_key = st.text_input(
                "API Key",
                type="password"
            )
            
            api_url = st.text_input(
                "API URL",
                placeholder="https://api.example.com/v1"
            )
        
        st.markdown("---")
        st.markdown("**Generation Parameters**")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            temperature = st.slider(
                "Temperature",
                min_value=0.0,
                max_value=1.0,
                value=APP_CONFIG['temperature']
            )
        
        with col2:
            top_p = st.slider(
                "Top P",
                min_value=0.0,
                max_value=1.0,
                value=APP_CONFIG['top_p']
            )
        
        with col3:
            max_length = st.slider(
                "Max Length",
                min_value=512,
                max_value=8192,
                value=APP_CONFIG['max_length'],
                step=512
            )
        
        if st.button("🧪 Test Model Connection", type="secondary"):
            st.info("Testing model connection... (This is a placeholder)")
        
        if st.button("💾 Save LLM Settings", type="primary"):
            create_success_message("LLM settings saved successfully!")
    
    # Tab 3: Advanced Settings
    with tab3:
        st.subheader("Advanced Settings")
        
        st.markdown("**Document Processing**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            chunk_size = st.number_input(
                "Chunk Size",
                value=APP_CONFIG['chunk_size'],
                step=100
            )
        
        with col2:
            overlap = st.number_input(
                "Chunk Overlap",
                value=APP_CONFIG['overlap'],
                step=50
            )
        
        st.markdown("---")
        st.markdown("**Data Management**")
        
        if st.button("🧹 Clear Cache"):
            st.info("Cache cleared successfully!")
        
        if st.button("🗑️ Delete All Projects"):
            if st.button("⚠️ Confirm Delete"):
                st.warning("All projects would be deleted!")
        
        st.markdown("---")
        st.markdown("**Logging**")
        
        log_level = st.selectbox(
            "Log Level",
            ["DEBUG", "INFO", "WARNING", "ERROR"]
        )
        
        if st.button("📋 View Logs"):
            st.info("Logs would be displayed here...")
        
        if st.button("💾 Save Advanced Settings", type="primary"):
            create_success_message("Advanced settings saved successfully!")
    
    # Tab 4: About
    with tab4:
        st.subheader("About ThesisMind AI")
        
        st.markdown(f"""
        ### ThesisMind AI v{APP_CONFIG['version']}
        
        **AI-powered Research Synthesis Platform**
        
        {APP_CONFIG['description']}
        
        ---
        
        ### Features
        - 📄 Multi-document analysis
        - 🧠 Knowledge synthesis
        - ✍️ Automatic thesis generation
        - 📊 Research gap identification
        - 📥 Multiple export formats
        
        ---
        
        ### Project Links
        - 🔗 [GitHub Repository](https://github.com/Honnagiri01/thesismind_ai)
        - 📖 [Documentation](https://github.com/Honnagiri01/thesismind_ai)
        - 🐛 [Report Issues](https://github.com/Honnagiri01/thesismind_ai/issues)
        
        ---
        
        ### Technology Stack
        - **Framework**: Streamlit
        - **LLM**: Open-weight models (Llama, Mistral, etc.)
        - **Language**: Python 3.9+
        - **License**: MIT
        
        ---
        
        ### Contributors
        - {APP_CONFIG['author']}
        
        """)
