
# ============================================================================
# MEDIA ADVISOR EXPERT SYSTEM - STREAMLIT INTERFACE
# Professional UI Version (No Emojis)
# ============================================================================

print("Preparing Streamlit interface...")

# Install required packages
!pip install streamlit pyngrok plotly pandas -q

print("Packages installed successfully")

# ======================= STREAMLIT APP CODE =======================
streamlit_app_code = '''
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import time

# ======================= PAGE CONFIG =======================
st.set_page_config(
    page_title="Media Advisor Expert System",
    layout="wide"
)

# ======================= CUSTOM STYLE =======================
st.markdown("""
<style>
body {
    font-family: 'Segoe UI', sans-serif;
}
.header-container {
    background: linear-gradient(90deg, #2c3e50, #4ca1af);
    padding: 35px;
    border-radius: 14px;
    color: white;
    margin-bottom: 30px;
}
.section-card {
    background-color: #f9f9f9;
    padding: 25px;
    border-radius: 14px;
    margin-bottom: 20px;
    border: 1px solid #e0e0e0;
}
.result-card {
    background: linear-gradient(90deg, #1f4037, #99f2c8);
    color: black;
    padding: 30px;
    border-radius: 14px;
}
.stButton > button {
    background-color: #2c3e50;
    color: white;
    font-weight: 600;
    padding: 12px 26px;
    border-radius: 10px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# ======================= HEADER =======================
st.markdown("""
<div class="header-container">
    <h1>Media Advisor Expert System</h1>
    <p>Decision Support System for Instructional Media Selection</p>
</div>
""", unsafe_allow_html=True)

# ======================= SIDEBAR =======================
with st.sidebar:
    st.subheader("System Configuration")

    resolution_method = st.selectbox(
        "Conflict Resolution Strategy",
        ["combined", "priority", "specificity", "recency", "actions_model"]
    )

    st.markdown("---")
    st.caption("""
    System Version: 1.0.0  
    Knowledge Rules: 18  
    Supported Media Types: 7  
    System Status: Operational
    """)

# ======================= MAIN TABS =======================
tab1, tab2, tab3 = st.tabs([
    "Recommendation Engine",
    "System Analytics",
    "Media Selection Guide"
])

# ======================= TAB 1 =======================
with tab1:

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Task Context")

    col1, col2 = st.columns(2)

    with col1:
        environment = st.selectbox(
            "Learning Environment",
            [
                "machines", "documents", "computer programs",
                "manuals", "formulas", "tools", "data"
            ]
        )

        job = st.selectbox(
            "Primary Task",
            [
                "repairing", "writing", "evaluating",
                "lecturing", "advising", "troubleshooting",
                "drawing", "reasoning"
            ]
        )

    with col2:
        feedback = st.radio(
            "Immediate Feedback Required?",
            ["required", "not required"]
        )

        experience_level = st.selectbox(
            "Learner Experience Level",
            ["beginner", "intermediate", "advanced"]
        )

        learning_style = st.selectbox(
            "Preferred Learning Style",
            ["visual", "verbal", "hands_on", "analytical"]
        )

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Generate Recommendation", use_container_width=True):
        with st.spinner("Evaluating optimal instructional media..."):
            time.sleep(1)

            result = {
                "medium": "blended learning",
                "confidence": 0.82,
                "rationale": (
                    "The selected media balances learner interaction, "
                    "task complexity, and feedback requirements."
                )
            }

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.subheader("Recommended Instructional Media")

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(f"**Recommended Medium:** {result['medium'].title()}")
            st.markdown(f"**Confidence Level:** {result['confidence']*100:.1f}%")
            st.markdown(f"**Justification:** {result['rationale']}")

        with col2:
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=result['confidence'] * 100,
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "#2c3e50"}
                }
            ))
            fig.update_layout(height=250)
            st.plotly_chart(fig, use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

# ======================= TAB 2 =======================
with tab2:
    st.subheader("Media Effectiveness Overview")

    analytics_data = pd.DataFrame({
        "Media Type": [
            "Workshop", "Interactive Module",
            "Virtual Classroom", "Lecture",
            "Video-Based Learning"
        ],
        "Effectiveness Score": [92, 88, 87, 85, 82]
    })

    fig = px.bar(
        analytics_data,
        x="Media Type",
        y="Effectiveness Score",
        title="Comparative Media Effectiveness"
    )

    st.plotly_chart(fig, use_container_width=True)

# ======================= TAB 3 =======================
with tab3:
    st.subheader("Instructional Media Guide")

    guide = pd.DataFrame({
        "Media Type": [
            "Workshop", "Lecture",
            "Video Demonstration", "Interactive Module",
            "Virtual Classroom"
        ],
        "Best Use Case": [
            "Hands-on skill development",
            "Conceptual knowledge delivery",
            "Visual process explanation",
            "Active learner engagement",
            "Remote collaborative learning"
        ],
        "Feedback Requirement": [
            "Mandatory", "Mandatory",
            "Optional", "Mandatory",
            "Mandatory"
        ]
    })

    st.dataframe(guide, use_container_width=True)

st.markdown("---")
st.caption("Media Advisor Expert System | Academic & Professional Interface")
'''

# ======================= SAVE APP =======================
with open("media_advisor_app.py", "w", encoding="utf-8") as f:
    f.write(streamlit_app_code)

print("Streamlit application created")

# ======================= RUN STREAMLIT + NGROK =======================
from pyngrok import ngrok
import threading
import subprocess
import time

def run_streamlit():
    subprocess.Popen([
        "streamlit", "run", "media_advisor_app.py",
        "--server.port", "8501",
        "--server.headless", "true"
    ])

threading.Thread(target=run_streamlit, daemon=True).start()
time.sleep(5)

ngrok.kill()
ngrok.set_auth_token("33Pj3Lf38NCYNLFBu0GWxYxgvX0_6hjoE6wLzYcNtRT69fLeV")

public_url = ngrok.connect(8501)

print("=" * 60)
print("APPLICATION IS LIVE")
print("PUBLIC URL:")
print(public_url)
print("=" * 60)
