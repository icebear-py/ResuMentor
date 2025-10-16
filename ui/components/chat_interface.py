import streamlit as st

def display_chat_interface(user_role, session_id):
    if (user_role == "I'm applying for the job (Screen and cover missing skills)" and
            st.session_state.learning_path and
            "error" not in st.session_state.learning_path):

        st.markdown("---")
        
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <div style="font-size: 2rem; margin-right: 1rem;">🤖</div>
            <div>
                <h2 style="color: #2E86AB; margin: 0;">AI Tutor Assistant</h2>
                <p style="color: #888; margin: 0; font-size: 0.9rem;">Ask questions about your learning path, skills, or career development!</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <style>
        .fixed-chat-box {
            height: 450px;
            overflow-y: auto;
            overflow-x: hidden;
            padding: 1.5rem;
            background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
            border-radius: 15px;
            border: 2px solid #333;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }
        .fixed-chat-box::-webkit-scrollbar {
            width: 10px;
        }
        .fixed-chat-box::-webkit-scrollbar-track {
            background: #1a1a1a;
            border-radius: 10px;
        }
        .fixed-chat-box::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #2E86AB 0%, #1B5E7A 100%);
            border-radius: 10px;
        }
        .fixed-chat-box::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #1B5E7A 0%, #0E4A5F 100%);
        }
        @keyframes blink {
            0%, 20% { opacity: 0; }
            50% { opacity: 1; }
            100% { opacity: 0; }
        }
        </style>
        """, unsafe_allow_html=True)

        messages_html = '<div class="fixed-chat-box" id="chatBox">'
        
        if st.session_state.chat_messages:
            for message in st.session_state.chat_messages:
                content = str(message["content"]).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')
                
                if message["role"] == "user":
                    messages_html += f'<div style="display: flex; justify-content: flex-end; margin: 1rem 0;"><div style="background: linear-gradient(135deg, #2E86AB 0%, #1B5E7A 100%); color: white; padding: 1rem 1.5rem; border-radius: 20px 20px 5px 20px; max-width: 70%; word-wrap: break-word; box-shadow: 0 4px 15px rgba(46, 134, 171, 0.3);"><div style="font-weight: 400; line-height: 1.5;">{content}</div><div style="font-size: 0.75rem; opacity: 0.9; margin-top: 0.5rem; text-align: right;">You</div></div></div>'
                else:
                    messages_html += f'<div style="display: flex; justify-content: flex-start; margin: 1rem 0;"><div style="background: linear-gradient(135deg, #2a2a2a 0%, #1f1f1f 100%); color: white; padding: 1rem 1.5rem; border-radius: 20px 20px 20px 5px; max-width: 70%; word-wrap: break-word; box-shadow: 0 4px 15px rgba(0,0,0,0.3); border: 1px solid #404040;"><div style="font-weight: 400; line-height: 1.5;">{content}</div><div style="font-size: 0.75rem; opacity: 0.8; margin-top: 0.5rem; color: #2E86AB;">AI Tutor</div></div></div>'
        else:
            messages_html += '<div style="text-align: center; padding: 3rem 2rem; color: #888; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center;"><div style="font-size: 4rem; margin-bottom: 1rem;">💬</div><h3 style="color: #2E86AB; margin-bottom: 0.5rem;">Start a conversation!</h3><p style="color: #999;">Ask me anything about your learning path, skills, or career development.</p></div>'

        if st.session_state.get("is_ai_typing", False):
            messages_html += '<div style="display: flex; justify-content: flex-start; margin: 1rem 0;"><div style="background: linear-gradient(135deg, #2a2a2a 0%, #1f1f1f 100%); color: #2E86AB; padding: 1rem 1.5rem; border-radius: 20px 20px 20px 5px; box-shadow: 0 4px 15px rgba(46, 134, 171, 0.2); border: 1px solid #2E86AB; font-style: italic; display: flex; align-items: center;"><span style="margin-right: 0.5rem;">🤖</span><span>AI is thinking</span><span style="animation: blink 1.4s infinite;">.</span><span style="animation: blink 1.4s infinite 0.2s;">.</span><span style="animation: blink 1.4s infinite 0.4s;">.</span></div></div>'

        messages_html += '</div>'
        
        st.markdown(messages_html, unsafe_allow_html=True)
        
        st.components.v1.html(
            """
            <script>
            const scrollToBottom = () => {
                const chatBox = window.parent.document.getElementById('chatBox');
                if (chatBox) {
                    chatBox.scrollTop = chatBox.scrollHeight;
                }
            };
            
            setTimeout(scrollToBottom, 100);
            setTimeout(scrollToBottom, 300);
            setTimeout(scrollToBottom, 500);
            </script>
            """,
            height=0,
        )

        st.markdown("---")
        
        with st.form(key="chat_form", clear_on_submit=True):
            col1, col2 = st.columns([6, 1])
            
            with col1:
                user_message = st.text_input(
                    "Type your message here...",
                    placeholder="💬 Ask about your learning path, skills, or career advice... (Press Enter to send)",
                    key="chat_input_field",
                    label_visibility="collapsed"
                )
            
            with col2:
                send_button = st.form_submit_button("📤", use_container_width=True, help="Send message")

        if send_button and user_message and user_message.strip():
            st.session_state.chat_messages.append({
                "role": "user",
                "content": user_message.strip()
            })
            
            st.session_state.is_ai_typing = True
            
            st.rerun()
        
        if st.session_state.get("is_ai_typing", False):
            from api_client import chat_with_tutor
            
            last_user_message = None
            for msg in reversed(st.session_state.chat_messages):
                if msg["role"] == "user":
                    last_user_message = msg["content"]
                    break
            
            if last_user_message:
                chat_result = chat_with_tutor(session_id, last_user_message)

                if chat_result and "reply" in chat_result:
                    ai_response = chat_result["reply"]
                    st.session_state.chat_messages.append({
                        "role": "assistant",
                        "content": ai_response
                    })
                else:
                    st.session_state.chat_messages.append({
                        "role": "assistant",
                        "content": "Sorry, I couldn't process your message. Please try again."
                    })

            st.session_state.is_ai_typing = False
            
            st.rerun()