import streamlit as st
from api_client import create_session, screen_resume
from components.screening_results import display_screening_results
from components.learning_path import display_learning_path
from components.chat_interface import display_chat_interface
from styles import get_custom_css

st.set_page_config(
    page_title="ResuMentor",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

def main():
    if "session_id" not in st.session_state:
        st.session_state.session_id = None
    if "screening_result" not in st.session_state:
        st.session_state.screening_result = None

    if "learning_path" not in st.session_state:
        st.session_state.learning_path = None

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    if "is_screening" not in st.session_state:
        st.session_state.is_screening = False

    if "is_generating_path" not in st.session_state:
        st.session_state.is_generating_path = False

    st.markdown('<h1 class="main-header">📄 ResuMentor : Screening & learning path generating agent</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem; color: #666; font-size: 1.4rem;">
        Resume screening agent for recruiters and job seekers applying for job.
        Screen the resume according to job description or if you're a job seeker
        you can use it to cover missing skills according to the job description by generating personalized learning path along with free youtube resources.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### 📁 Upload Your Resume")

        uploaded_file = st.file_uploader(
            "Choose your resume file",
            type=['pdf', 'docx', 'doc'],
            help="Upload your resume in PDF or DOCX format",
            label_visibility="collapsed"
        )

        st.markdown("---")
        st.markdown("### 👤 Select Your Role")

        user_role = st.radio(
            "Choose your role:",
            ["I'm a recruiter (Screen resume only) ", "I'm applying for the job (Screen and cover missing skills)"],
            key="user_role",
            label_visibility="collapsed"
        )

    with col2:
        st.markdown("### 📝 Job Description")

        job_description = st.text_area(
            "Paste the job description here:",
            height=200,
            placeholder="Enter the job description, requirements, and qualifications...",
            label_visibility="collapsed"
        )

        st.markdown("---")
        screen_disabled = not uploaded_file or not job_description or st.session_state.is_screening

        if st.button(
                "🔍 Screen Resume" if not st.session_state.is_screening else "⏳ Screening...",
                disabled=screen_disabled,
                key="screen_button"
                
        ):

            st.session_state.is_screening = True
            with st.spinner("Analyzing resume and job requirements..."):
                st.session_state.session_id = create_session()
                result = screen_resume(st.session_state.session_id, job_description, uploaded_file)

            st.session_state.is_screening = False

            if result and "screen_result" in result:
                st.session_state.screening_result = result["screen_result"]
                st.success("✅ Resume screening completed!")
            else:
                st.error("❌ Failed to screen resume. Please try again.")

    display_screening_results(st.session_state.screening_result, user_role)

    display_learning_path(st.session_state.learning_path)

    display_chat_interface(user_role, st.session_state.session_id)

if __name__ == "__main__":
    main()