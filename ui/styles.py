def get_custom_css():
    return """
    <style>
        .stApp {
            background-color: #1a1a1a;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            background: transparent !important;
        }

        div[data-testid="stVerticalBlock"] > div,
        div[data-testid="column"] > div,
        div[data-testid="stHorizontalBlock"] > div,
        .element-container {
            background: transparent !important;
        }

        .stFileUploader, .stTextArea, .stRadio, .stMarkdown {
            background: transparent !important;
        }

        .stFileUploader > div,
        .stFileUploader > div > div,
        .stFileUploader section,
        .stFileUploader section > div {
            background: transparent !important;
            border: none !important;
        }

        .stTextArea > div,
        .stTextArea textarea {
            background: #2a2a2a !important;
            border: 2px solid #2E86AB !important;
            border-radius: 10px !important;
            color: #fff !important;
        }

        .stTextArea textarea::placeholder {
            color: #888 !important;
        }

        .stFileUploader section {
            border: 3px dashed #2E86AB !important;
            border-radius: 15px !important;
            padding: 2rem !important;
            background: #2a2a2a !important;
        }

        .stFileUploader section:hover {
            border-color: #1B5E7A !important;
            background: #333 !important;
        }

        .stRadio > div {
            background: transparent !important;
        }

        .stRadio label {
            color: #fff !important;
        }

        .main-header {
            text-align: center;
            font-size: 3rem;
            font-weight: bold;
            color: #2E86AB;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }

        .stMarkdown h3 {
            color: #2E86AB;
            margin-bottom: 1rem;
        }

        hr {
            border-color: #333;
            margin: 1.5rem 0;
        }

        .score-circle {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            font-weight: bold;
            color: white;
            margin: 0 auto;
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        }

        .score-good {
            background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
        }

        .score-medium {
            background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
        }

        .score-bad {
            background: linear-gradient(135deg, #F44336 0%, #C62828 100%);
        }

         .result-card {
             background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
             padding: 2rem;
             border-radius: 15px;
             box-shadow: 0 8px 32px rgba(0,0,0,0.3);
             margin: 1rem 0;
             border: 1px solid #333;
         }

         .metric-card {
             background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
             padding: 1.5rem;
             border-radius: 12px;
             box-shadow: 0 4px 20px rgba(0,0,0,0.2);
             margin: 0.5rem;
             border: 1px solid #333;
             text-align: center;
             transition: all 0.3s ease;
         }

         .metric-card:hover {
             transform: translateY(-2px);
             box-shadow: 0 8px 25px rgba(46, 134, 171, 0.2);
         }

         .metric-label {
             color: #888;
             font-size: 0.9rem;
             margin-bottom: 0.5rem;
             text-transform: uppercase;
             letter-spacing: 1px;
         }

         .metric-value {
             color: #fff;
             font-size: 1.8rem;
             font-weight: bold;
             margin-bottom: 0.5rem;
         }

         .metric-score-good {
             color: #4CAF50;
         }

         .metric-score-medium {
             color: #FF9800;
         }

         .metric-score-bad {
             color: #F44336;
         }

         .recommendation-card {
             background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
             padding: 2rem;
             border-radius: 15px;
             box-shadow: 0 8px 32px rgba(0,0,0,0.3);
             margin: 1rem 0;
             border: 2px solid #4CAF50;
             text-align: center;
         }

         .recommendation-card.reject {
             border-color: #F44336;
         }

         .recommendation-text {
             font-size: 1.5rem;
             font-weight: bold;
             margin-bottom: 0.5rem;
         }

         .recommendation-good {
             color: #4CAF50;
         }

         .recommendation-bad {
             color: #F44336;
         }

         .section-header {
             color: #2E86AB;
             font-size: 1.3rem;
             font-weight: bold;
             margin: 1.5rem 0 1rem 0;
             padding-bottom: 0.5rem;
             border-bottom: 2px solid #2E86AB;
         }

         .detailed-section {
             background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
             padding: 2rem;
             border-radius: 15px;
             box-shadow: 0 8px 32px rgba(0,0,0,0.3);
             margin: 1rem 0;
             border: 1px solid #333;
         }

         .detail-item {
             margin: 1rem 0;
             padding: 1rem;
             background: #333;
             border-radius: 8px;
             border-left: 4px solid #2E86AB;
         }

         .detail-label {
             color: #2E86AB;
             font-weight: bold;
             margin-bottom: 0.5rem;
             font-size: 1.1rem;
         }

         .detail-content {
             color: #fff;
             line-height: 1.6;
         }

         .red-flag-item {
             background: #4a1a1a;
             border-left-color: #F44336;
         }

         .red-flag-label {
             color: #F44336;
         }

        .skill-gap {
            background: #ffebee;
            color: #c62828;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            margin: 0.25rem;
            display: inline-block;
            font-weight: bold;
        }

        .skill-strength {
            background: #e8f5e8;
            color: #2e7d32;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            margin: 0.25rem;
            display: inline-block;
            font-weight: bold;
        }

        .learning-path-card {
            background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            margin: 1rem 0;
            border: 1px solid #333;
            color: #fff;
        }

        .day-card {
            background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
            border-left: 5px solid #2E86AB;
            border: 1px solid #333;
            color: #fff;
        }

        .day-card h4 {
            color: #2E86AB;
            margin-bottom: 1rem;
        }

        .day-card p {
            color: #fff;
        }

        .day-card ul {
            color: #fff;
        }

        .day-card li {
            color: #fff;
            margin: 0.5rem 0;
        }

        .activity-box {
            background: #333;
            padding: 1rem;
            border-radius: 8px;
            margin: 0.5rem 0;
            border-left: 4px solid #2E86AB;
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .resource-box {
            background: #333;
            padding: 1rem;
            border-radius: 8px;
            margin: 0.5rem 0;
            border-left: 4px solid #FF9800;
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .type-label {
            background: #2E86AB;
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 15px;
            font-size: 0.8rem;
            font-weight: bold;
            min-width: 80px;
            text-align: center;
        }

        .resource-label {
            background: #FF9800;
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 15px;
            font-size: 0.8rem;
            font-weight: bold;
            min-width: 80px;
            text-align: center;
        }

        .activity-text, .resource-text {
            color: #FFFFFF !important;
            flex: 1;
            font-weight: 500;
        }

        .chat-container {
            background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            border: 1px solid #333;
            min-height: 400px;
            max-height: 600px;
            overflow-y: auto;
        }

        .chat-message {
            padding: 1rem;
            margin: 0.5rem 0;
            border-radius: 15px;
            max-width: 80%;
        }

        .user-message {
            background: linear-gradient(135deg, #2E86AB 0%, #1B5E7A 100%);
            color: white;
            margin-left: auto;
            text-align: right;
            border-radius: 20px 20px 5px 20px;
            box-shadow: 0 4px 15px rgba(46, 134, 171, 0.3);
        }

        .ai-message {
            background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
            color: white;
            margin-right: auto;
            border-radius: 20px 20px 20px 5px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            border: 1px solid #333;
        }

        .chat-input-container {
            background: #2a2a2a;
            border-radius: 25px;
            padding: 0.5rem;
            border: 2px solid #2E86AB;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .chat-input {
            background: transparent;
            border: none;
            color: white;
            flex: 1;
            padding: 0.75rem 1rem;
            outline: none;
        }

        .chat-input::placeholder {
            color: #888;
        }

        .send-button {
            background: linear-gradient(135deg, #2E86AB 0%, #1B5E7A 100%);
            border: none;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .send-button:hover {
            transform: scale(1.1);
            box-shadow: 0 4px 15px rgba(46, 134, 171, 0.4);
        }

        .typing-indicator {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: #888;
            font-style: italic;
        }

        .typing-dots {
            display: flex;
            gap: 0.25rem;
        }

        .typing-dot {
            width: 6px;
            height: 6px;
            background: #2E86AB;
            border-radius: 50%;
            animation: typing 1.4s infinite;
        }

        .typing-dot:nth-child(2) {
            animation-delay: 0.2s;
        }

        .typing-dot:nth-child(3) {
            animation-delay: 0.4s;
        }

        @keyframes typing {
            0%, 60%, 100% {
                transform: translateY(0);
            }
            30% {
                transform: translateY(-10px);
            }
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .stButton > button {
            background: linear-gradient(135deg, #2E86AB 0%, #1B5E7A 100%);
            color: white;
            border: none;
            padding: 0.75rem 2rem;
            border-radius: 25px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(46, 134, 171, 0.4);
        }

         .stButton > button:disabled {
             background: #555 !important;
             color: #999 !important;
             cursor: not-allowed;
             transform: none;
             box-shadow: none;
         }
    </style>
    """