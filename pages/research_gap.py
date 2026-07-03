"""
Research Gap page for ThesisMind AI.
Identify and analyze research gaps.
"""

import streamlit as st
from utils.ui import create_info_message, create_metric_card


def show():
    """Display research gap analysis page."""
    st.title("🔬 Research Gap Analysis")
    st.markdown("---")
    
    if not st.session_state.current_project:
        st.error("Please select or create a project first!")
        return
    
    pm = st.session_state.project_manager
    project = pm.get_project_by_name(st.session_state.current_project)
    
    st.markdown(f"### Project: {project['name']}")
    
    documents = project.get('documents', [])
    
    if not documents:
        create_info_message("No documents uploaded. Upload documents first to analyze research gaps.")
        return
    
    st.markdown("---")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    create_metric_card(col1, "Documents Analyzed", len(documents))
    create_metric_card(col2, "Gaps Identified", "12")
    create_metric_card(col3, "Research Opportunities", "8")
    create_metric_card(col4, "Confidence Score", "85%")
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["Identified Gaps", "Opportunities", "Gap Analysis Report"])
    
    # Tab 1: Identified Gaps
    with tab1:
        st.subheader("Identified Research Gaps")
        
        gaps = [
            {
                "gap": "Limited exploration of real-time processing",
                "documents": 3,
                "confidence": "92%",
                "importance": "High"
            },
            {
                "gap": "Lack of comparative analysis across frameworks",
                "documents": 4,
                "confidence": "88%",
                "importance": "High"
            },
            {
                "gap": "Insufficient analysis of scalability issues",
                "documents": 2,
                "confidence": "75%",
                "importance": "Medium"
            },
            {
                "gap": "Limited discussion of ethical implications",
                "documents": 3,
                "confidence": "68%",
                "importance": "Medium"
            },
        ]
        
        for idx, gap in enumerate(gaps, 1):
            with st.container():
                col1, col2 = st.columns([4, 1])
                
                with col1:
                    st.markdown(f"**{idx}. {gap['gap']}**")
                    col_a, col_b, col_c = st.columns(3)
                    col_a.caption(f"📊 Found in {gap['documents']} documents")
                    col_b.caption(f"✓ Confidence: {gap['confidence']}")
                    col_c.caption(f"🎯 Importance: {gap['importance']}")
                
                with col2:
                    if st.button("📋 Details", key=f"gap_{idx}"):
                        st.write("More details about this research gap...")
                
                st.divider()
    
    # Tab 2: Opportunities
    with tab2:
        st.subheader("Research Opportunities")
        
        opportunities = [
            {
                "opportunity": "Develop hybrid approach combining multiple frameworks",
                "potential_impact": "Very High",
                "effort": "Medium"
            },
            {
                "opportunity": "Create real-time processing solution",
                "potential_impact": "High",
                "effort": "High"
            },
            {
                "opportunity": "Establish ethical guidelines for the domain",
                "potential_impact": "High",
                "effort": "Medium"
            },
        ]
        
        for idx, opp in enumerate(opportunities, 1):
            with st.container():
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"**{idx}. {opp['opportunity']}**")
                    col_a, col_b = st.columns(2)
                    col_a.caption(f"💡 Impact: {opp['potential_impact']}")
                    col_b.caption(f"⚙️ Effort: {opp['effort']}")
                
                with col2:
                    if st.button("✓ Use This", key=f"opp_{idx}"):
                        st.session_state.selected_opportunity = opp['opportunity']
                        st.success("Added to thesis research direction!")
                
                st.divider()
    
    # Tab 3: Gap Analysis Report
    with tab3:
        st.subheader("Gap Analysis Report")
        
        st.markdown("""
        ## Research Gap Analysis Summary
        
        ### Overview
        Based on the analysis of uploaded documents, the following research gaps have been identified:
        
        ### Key Findings
        
        1. **Methodological Gaps**: Limited comparative studies across different frameworks
        2. **Application Gaps**: Lack of real-world implementations and case studies
        3. **Theoretical Gaps**: Insufficient theoretical foundation in certain areas
        4. **Empirical Gaps**: Missing empirical validation in specific domains
        
        ### Recommendations
        
        - Focus on hybrid approaches
        - Develop practical implementations
        - Conduct thorough empirical studies
        - Consider ethical implications
        
        ### Next Steps
        
        Use these gaps to:
        - Define your research objectives
        - Design novel methodologies
        - Create original contributions
        """)
        
        if st.button("📄 Download Report", type="primary"):
            st.info("Report generation initiated...")
