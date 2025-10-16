# ResuMentor UI

A beautiful and fully functional Streamlit UI for the ResuMentor application.

## Features

- **📄 Resume Upload**: Drag and drop or click to upload PDF/DOCX resumes
- **👤 Role Selection**: Choose between "Recruiter" or "Job Applicant"
- **🔍 AI Screening**: Get detailed resume analysis with visual score indicators
- **🎯 Learning Path**: Personalized 7-day learning plans for skill gaps
- **💬 AI Chat**: Interactive chat with AI tutor for career guidance

## Visual Features

- **Dynamic Score Circle**: 
  - 🟢 Green for good scores (70+)
  - 🟠 Orange for medium scores (50-69)
  - 🔴 Red for poor scores (<50)
- **Skill Tags**: Missing skills highlighted in red, strengths in green
- **Responsive Design**: Beautiful gradients and animations
- **Loading States**: Visual feedback during processing

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure your backend API is running on `http://localhost:8000`

3. Run the Streamlit app:
```bash
streamlit run app.py
```

## Usage

1. **Upload Resume**: Upload your resume in PDF or DOCX format
2. **Select Role**: Choose "I'm a recruiter" or "I'm applying for the job"
3. **Enter Job Description**: Paste the job description and requirements
4. **Screen Resume**: Click "Screen Resume" to get AI analysis
5. **View Results**: See your fit score, strengths, and missing skills
6. **Generate Learning Path**: (Job applicants only) Click "Cover Up My Missing Skills"
7. **Chat with AI**: Ask questions about your learning path or career

## Backend Integration

The UI connects to the following API endpoints:
- `POST /session/` - Create session
- `POST /screen/` - Screen resume
- `POST /plan/` - Generate learning path
- `POST /chat/` - Chat with AI tutor

## Customization

The UI uses custom CSS for styling. You can modify the styles in the `st.markdown()` section at the top of `app.py` to customize colors, fonts, and layouts.
