import streamlit as st

def escape_html(text):
    if not text:
        return ""
    return str(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#x27;')

def validate_youtube_url(url):
    if not url or not isinstance(url, str):
        return False
    return url.startswith(('https://www.youtube.com/watch?v=', 'https://www.youtube.com/playlist?list='))

def generate_youtube_resources_html(resources_data):
    if not resources_data or not isinstance(resources_data, dict):
        return ""
    
    try:
        videos = resources_data.get("videos", [])
        playlists = resources_data.get("playlists", [])
        
        if not videos and not playlists:
            return ""
        
        html = '<div class="youtube-resources-container">'
        html += '<div class="youtube-resources-title">📺 YouTube Resources</div>'
        html += '<div class="youtube-resources-grid">'
        
        for video in videos[:2]:
            if not isinstance(video, dict):
                continue
                
            title = escape_html(video.get("title", ""))
            channel = escape_html(video.get("channel", ""))
            url = video.get("url", "")
            
            if not validate_youtube_url(url):
                continue
            
            html += f'''<a href="{escape_html(url)}" target="_blank" class="youtube-resource-card">
                <div class="youtube-resource-title">{title}</div>
                <div class="youtube-resource-meta">
                    <span class="youtube-resource-type">Video</span>
                </div>
            </a>'''
        
        for playlist in playlists[:2]:
            if not isinstance(playlist, dict):
                continue
                
            title = escape_html(playlist.get("title", ""))
            channel = escape_html(playlist.get("channel", ""))
            url = playlist.get("url", "")
            
            if not validate_youtube_url(url):
                continue
            
            html += f'''<a href="{escape_html(url)}" target="_blank" class="youtube-resource-card">
                <div class="youtube-resource-title">{title}</div>
                <div class="youtube-resource-meta">
                    <span class="youtube-resource-type playlist">Playlist</span>
                </div>
            </a>'''
        
        html += '</div></div>'
        return html
        
    except Exception as e:
        return ""

def display_learning_path(path):
    if not path:
        return

    st.markdown("---")
    st.markdown("## 🛤️ Generated Learning Path")

    st.markdown("""
    <style>
    .youtube-resources-container {
        background: transparent;
        border-radius: 6px;
        padding: 0.5rem 0;
        margin-top: 0.75rem;
        border: none;
    }
    .youtube-resources-title {
        color: #2E86AB;
        font-size: 0.9rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.25rem;
    }
    .youtube-resources-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 0.5rem;
    }
    .youtube-resource-card {
        background: #2a2a2a;
        border: 1px solid #404040;
        border-radius: 6px;
        padding: 0.5rem;
        text-decoration: none;
        transition: all 0.3s ease;
        display: block;
    }
    .youtube-resource-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(46, 134, 171, 0.2);
        border-color: #2E86AB;
    }
    .youtube-resource-title {
        color: #fff;
        font-weight: 500;
        font-size: 0.8rem;
        margin-bottom: 0.25rem;
        line-height: 1.3;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    .youtube-resource-meta {
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }
    .youtube-resource-type {
        background: #2E86AB;
        color: white;
        padding: 0.15rem 0.5rem;
        border-radius: 8px;
        font-size: 0.7rem;
        font-weight: bold;
    }
    .youtube-resource-type.playlist {
        background: #FF9800;
    }
    </style>
    """, unsafe_allow_html=True)

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

    if "error" in path:
        st.error(f"Error: {path['error']}")
        if "raw_output" in path:
            st.text("Raw output:")
            st.text(path["raw_output"])
        return

    if "summary" in path:
        st.markdown("### 📝 Plan Summary")
        st.markdown(f'<div class="learning-path-card">{path["summary"]}</div>', unsafe_allow_html=True)

    if "days" in path and path["days"]:
        st.markdown("### 📅 Daily Learning Schedule")

        for day_data in path["days"]:
            day_num = day_data.get("day", 1)
            focus = day_data.get("focus", "")
            activities = day_data.get("activities", [])
            resources = day_data.get("resources", [])

            day_content = f'<div class="day-card"><h4 style="color: #2E86AB; margin-bottom: 1rem;">Day {escape_html(day_num)}: {escape_html(focus)}</h4>'

            all_items = []

            if activities:
                for activity in activities:
                    if isinstance(activity, dict):
                        activity_type = activity.get("type", "ACTIVITY")
                        activity_desc = activity.get("description", str(activity))
                        duration = activity.get("duration_minutes", "")
                        outcome = activity.get("outcome", "")
                    else:
                        activity_type = "ACTIVITY"
                        activity_desc = str(activity)
                        duration = ""
                        outcome = ""
                    all_items.append((activity_type, activity_desc, duration, outcome, "activity"))

            youtube_resources_list = []
            if resources:
                for resource in resources:
                    if isinstance(resource, dict) and "videos" in resource and "playlists" in resource:
                        youtube_resources_list.append(resource)
                        continue
                    
                    if isinstance(resource, dict):
                        resource_type = resource.get("type", "RESOURCE")
                        resource_desc = resource.get("description", str(resource))
                        duration = resource.get("duration_minutes", "")
                        outcome = resource.get("outcome", "")
                    else:
                        resource_type = "RESOURCE"
                        resource_desc = str(resource)
                        duration = ""
                        outcome = ""
                    all_items.append((resource_type, resource_desc, duration, outcome, "resource"))

            activity_count = 0
            for item_type, item_desc, duration, outcome, item_category in all_items:
                if item_category == "activity":
                    duration_html = f'<div style="color: #888; font-size: 0.9rem;">⏱️ {escape_html(duration)} minutes</div>' if duration else ''
                    outcome_html = f'<div style="color: #4CAF50; font-size: 0.9rem; margin-top: 0.5rem;">✅ {escape_html(outcome)}</div>' if outcome else ''
                    
                    day_content += f'<div class="activity-box"><div class="type-label">{escape_html(item_type)}</div><div class="activity-text"><div style="font-weight: bold; margin-bottom: 0.5rem;">{escape_html(item_desc)}</div>{duration_html}{outcome_html}'
                    
                    if activity_count < len(youtube_resources_list):
                        youtube_resources_html = generate_youtube_resources_html(youtube_resources_list[activity_count])
                        if youtube_resources_html:
                            day_content += youtube_resources_html
                        activity_count += 1
                    
                    day_content += '</div></div>'
                else:
                    duration_html = f'<div style="color: #888; font-size: 0.9rem;">⏱️ {escape_html(duration)} minutes</div>' if duration else ''
                    outcome_html = f'<div style="color: #4CAF50; font-size: 0.9rem; margin-top: 0.5rem;">✅ {escape_html(outcome)}</div>' if outcome else ''
                    day_content += f'<div class="resource-box"><div class="resource-label">{escape_html(item_type)}</div><div class="resource-text"><div style="font-weight: bold; margin-bottom: 0.5rem;">{escape_html(item_desc)}</div>{duration_html}{outcome_html}</div></div>'

            day_content += "</div>"
            st.markdown(day_content, unsafe_allow_html=True)

    if "next_steps" in path and path["next_steps"]:
        st.markdown("### 🚀 Next Steps & Future Development")
        
        next_steps = path["next_steps"]
        
        next_steps_html = '<div class="result-card"><div style="margin-top: 0.5rem;">'
        
        if "week_2" in next_steps and next_steps["week_2"]:
            week_2_text = str(next_steps["week_2"]).replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
            next_steps_html += '<div style="margin-bottom: 1.5rem;"><div style="color: #2E86AB; font-weight: bold; margin-bottom: 0.5rem; font-size: 1.1rem;">📅 Week 2 Continuation</div><div style="color: #fff; line-height: 1.6;">' + week_2_text + '</div></div>'
        
        if "portfolio_project" in next_steps and next_steps["portfolio_project"]:
            portfolio_text = str(next_steps["portfolio_project"]).replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
            next_steps_html += '<div style="margin-bottom: 1.5rem;"><div style="color: #2E86AB; font-weight: bold; margin-bottom: 0.5rem; font-size: 1.1rem;">💼 Portfolio Project</div><div style="color: #fff; line-height: 1.6;">' + portfolio_text + '</div></div>'
        
        if "long_term" in next_steps and next_steps["long_term"]:
            long_term_text = str(next_steps["long_term"]).replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
            next_steps_html += '<div style="margin-bottom: 1.5rem;"><div style="color: #2E86AB; font-weight: bold; margin-bottom: 0.5rem; font-size: 1.1rem;">🎯 Long-term Development (3-6 months)</div><div style="color: #fff; line-height: 1.6;">' + long_term_text + '</div></div>'
        
        next_steps_html += '</div></div>'
        
        st.markdown(next_steps_html, unsafe_allow_html=True)