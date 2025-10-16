import streamlit as st
import requests

API_BASE_URL = "https://resumentor.up.railway.app"

def create_session():
    try:
        resp = requests.post(f"{API_BASE_URL}/session/")
        if resp.status_code == 200:
            return resp.json()["session_id"]
        else:
            st.error("Failed to create session")
            return None
    except Exception as e:
        st.error(f"Error creating session: {str(e)}")
        return None

def screen_resume(session_id, job_description, resume_file):
    try:
        files = {"resume_file": resume_file}
        data = {
            "session_id": session_id,
            "job_description": job_description
        }

        resp = requests.post(f"{API_BASE_URL}/screen/", files=files, data=data)

        if resp.status_code == 200:
            return resp.json()
        else:
            st.error(f"Screening failed: {resp.text}")
            return None
    except Exception as e:
        st.error(f"Error screening resume: {str(e)}")
        return None

def generate_learning_path(session_id, gaps, missing_required_skills, missing_preferred_skills):
    try:
        data = {
            "session_id": session_id,
            "gaps": gaps,
            "missing_required_skills": missing_required_skills,
            "missing_preferred_skills": missing_preferred_skills
        }
        
        resp = requests.post(f"{API_BASE_URL}/plan/", data=data)
        
        if resp.status_code == 200:
            return resp.json()
        else:
            st.error(f"Learning path generation failed: {resp.text}")
            return None
    except Exception as e:
        st.error(f"Error generating learning path: {str(e)}")
        return None

def chat_with_tutor(session_id, msg):
    try:
        data = {
            "session_id": session_id,
            "msg": msg
        }

        resp = requests.post(f"{API_BASE_URL}/chat/", data=data, timeout=30)

        if resp.status_code == 200:
            return resp.json()
        else:
            st.error(f"Chat failed: {resp.text}")
            return None
    except requests.exceptions.Timeout:
        st.error("Chat request timed out. Please try again.")
        return None
    except Exception as e:
        st.error(f"Error chatting: {str(e)}")
        return None