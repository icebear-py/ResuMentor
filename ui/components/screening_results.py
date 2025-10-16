import streamlit as st

def get_score_color(score):
    if score >= 70:
        return "score-good"
    elif score >= 50:
        return "score-medium"
    else:
        return "score-bad"

def display_screening_results(result, user_role):
    if not result:
        return
    
    st.markdown("---")
    st.markdown("## 📊 Screening Results")
    
    st.markdown("""
    <script>
    setTimeout(function() {
        window.scrollTo({
            top: document.querySelector('[data-testid="stMarkdown"]').offsetTop - 100,
            behavior: 'smooth'
        });
    }, 500);
    </script>
    """, unsafe_allow_html=True)
    
    if "error" in result:
        st.error(f"Error: {result['error']}")
        if "raw_output" in result:
            st.text("Raw output:")
            st.text(result["raw_output"])
        return
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        score = result.get("fit_score", 0)
        score_class = get_score_color(score)
        
        st.markdown(f"""
        <div class="score-circle {score_class}">
            {score}%
        </div>
        <div style="text-align: center; margin-top: 1rem; font-size: 1.2rem; font-weight: bold; color: #fff;">
            OVERALL FIT SCORE
        </div>
        """, unsafe_allow_html=True)
        
        is_positive = score >= 60
        rec_class = "recommendation-good" if is_positive else "recommendation-bad"
        rec_card_class = "" if is_positive else "reject"
        
        hire_text = "✅ HIRE" if is_positive else "❌ DON'T HIRE"
        recommendation = result.get("recommendation")
        st.markdown(f"""
        <div class="recommendation-card {rec_card_class}" style="margin-top: 2rem;">
            <div class="recommendation-text {rec_class}">
                {hire_text}
            </div>
            <div style="color: #888; font-size: 0.9rem;">
                {recommendation}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        score_breakdown = result.get("score_breakdown", {})
        
        def get_score_color_class(score):
            if score >= 70:
                return "color: #4CAF50;"
            elif score >= 50:
                return "color: #FF9800;"
            else:
                return "color: #F44336;"
        
        tech_score = score_breakdown.get("technical_skills", 0)
        exp_score = score_breakdown.get("experience_relevance", 0)
        edu_score = score_breakdown.get("education", 0)
        soft_score = score_breakdown.get("soft_skills", 0)
        cult_score = score_breakdown.get("cultural_fit", 0)
        
        st.markdown(f"""
        <div class="result-card">
            <div class="section-header">📈 Performance Metrics</div>
            <div style="margin-top: 1rem;">
                <div style="margin: 0.5rem 0;"><strong>Technical Skills:</strong> <span style="{get_score_color_class(tech_score)}">{tech_score}</span></div>
                <div style="margin: 0.5rem 0;"><strong>Experience Relevance:</strong> <span style="{get_score_color_class(exp_score)}">{exp_score}</span></div>
                <div style="margin: 0.5rem 0;"><strong>Education:</strong> <span style="{get_score_color_class(edu_score)}">{edu_score}</span></div>
                <div style="margin: 0.5rem 0;"><strong>Soft Skills:</strong> <span style="{get_score_color_class(soft_score)}">{soft_score}</span></div>
                <div style="margin: 0.5rem 0;"><strong>Cultural Fit:</strong> <span style="{get_score_color_class(cult_score)}">{cult_score}</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">🔍 Detailed Assessment</div>', unsafe_allow_html=True)
    
    detail_col1, detail_col2 = st.columns(2)
    
    with detail_col1:
        if "summary" in result:
            st.markdown(f"""
            <div class="detail-item">
                <div class="detail-label">📋 Summary</div>
                <div class="detail-content">{result["summary"]}</div>
            </div>
            """, unsafe_allow_html=True)
        
        if "key_strengths" in result and result["key_strengths"]:
            strengths_html = ""
            for strength in result["key_strengths"]:
                strengths_html += f'<span class="skill-strength">{strength}</span>'
            st.markdown(f"""
            <div class="detail-item">
                <div class="detail-label">✅ Key Strengths</div>
                <div class="detail-content">{strengths_html}</div>
            </div>
            """, unsafe_allow_html=True)
        
        if "missing_required_skills" in result and result["missing_required_skills"]:
            missing_req_html = ""
            for skill in result["missing_required_skills"]:
                missing_req_html += f'<span class="skill-gap">{skill}</span>'
            st.markdown(f"""
            <div class="detail-item">
                <div class="detail-label">❌ Missing Required Skills</div>
                <div class="detail-content">{missing_req_html}</div>
            </div>
            """, unsafe_allow_html=True)
        
        if "missing_preferred_skills" in result and result["missing_preferred_skills"]:
            missing_pref_html = ""
            for skill in result["missing_preferred_skills"]:
                missing_pref_html += f'<span class="skill-gap">{skill}</span>'
            st.markdown(f"""
            <div class="detail-item">
                <div class="detail-label">⚠️ Missing Preferred Skills</div>
                <div class="detail-content">{missing_pref_html}</div>
            </div>
            """, unsafe_allow_html=True)
    
    with detail_col2:
        if "gaps" in result and result["gaps"]:
            gaps_html = ""
            for gap in result["gaps"]:
                gaps_html += f'<span class="skill-gap">{gap}</span>'
            st.markdown(f"""
            <div class="detail-item">
                <div class="detail-label">❌ Skill Gaps</div>
                <div class="detail-content">{gaps_html}</div>
            </div>
            """, unsafe_allow_html=True)
        
        if "red_flags" in result and result["red_flags"]:
            red_flags_html = ""
            for flag in result["red_flags"]:
                red_flags_html += f'<div style="color: #F44336; margin: 0.5rem 0;">⚠️ {flag}</div>'
            st.markdown(f"""
            <div class="detail-item red-flag-item">
                <div class="detail-label red-flag-label">🚩 Red Flags</div>
                <div class="detail-content">{red_flags_html}</div>
            </div>
            """, unsafe_allow_html=True)
        
        if "reasoning" in result:
            st.markdown(f"""
            <div class="detail-item">
                <div class="detail-label">🧠 Reasoning</div>
                <div class="detail-content">{result["reasoning"]}</div>
            </div>
            """, unsafe_allow_html=True)
        
        if "interview_focus_areas" in result and result["interview_focus_areas"]:
            focus_areas_html = ""
            for area in result["interview_focus_areas"]:
                focus_areas_html += f'<div style="color: #2E86AB; margin: 0.5rem 0;">🎯 {area}</div>'
            st.markdown(f"""
            <div class="detail-item">
                <div class="detail-label">🎯 Interview Focus Areas</div>
                <div class="detail-content">{focus_areas_html}</div>
            </div>
            """, unsafe_allow_html=True)

    if user_role == "I'm applying for the job (Screen and cover missing skills)" and ("gaps" in result and result["gaps"] or "missing_required_skills" in result and result["missing_required_skills"] or "missing_preferred_skills" in result and result["missing_preferred_skills"]):
        st.markdown("---")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown('<div style="color: #888; font-size: 1.3rem; margin-top: 0.5rem;">💡 Cover up these missing skills by generating a learning plan along with free resources. (May take upto 2 minutes) </div>', unsafe_allow_html=True)
        with col2:
            if st.button("🎯 Cover Up My Missing Skills", key="coverup_button"):
                st.session_state.is_generating_path = True

                with st.spinner("Generating personalized learning path..."):
                    gaps_str = ", ".join(result.get("gaps", []))
                    missing_required_str = ", ".join(result.get("missing_required_skills", []))
                    missing_preferred_str = ", ".join(result.get("missing_preferred_skills", []))
                    
                    from api_client import generate_learning_path
                    path_result = generate_learning_path(
                        st.session_state.session_id, 
                        gaps_str, 
                        missing_required_str, 
                        missing_preferred_str
                    )

                st.session_state.is_generating_path = False

                if path_result and "learning_plan" in path_result:
                    st.session_state.learning_path = path_result["learning_plan"]
                    st.success("✅ Learning path generated successfully!")
                else:
                    st.error("❌ Failed to generate learning path. Please try again.")