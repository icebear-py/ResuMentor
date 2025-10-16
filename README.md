# ResuMentor 🤖📄

An intelligent AI-powered resume screening and learning path generation agentic platform with integrated chatbot designed for both recruiters and job seekers.

**For Recruiters**: Efficiently analyze and screen resumes against job descriptions to identify the most suitable candidates with detailed scoring and insights.

**For Job Seekers**: Evaluate resumes to highlight missing skills based on target job descriptions and generate personalized learning paths with curated free YouTube resources for skill development.

## Key Features

### Core Functionality
- ** Resume Upload**: Drag and drop or click to upload PDF/DOCX resumes
- ** Role Selection**: Choose between "Recruiter" or "Job Applicant" modes
- ** AI Screening**: Get detailed resume analysis with visual score indicators
- ** Learning Path**: Personalized 7-day learning plans for covering skill gaps
- ** AI Chat**: Interactive chat with AI tutor for career guidance

### Visual Experience
- **Dynamic Score Circle**: 
  -  Green for excellent scores (70+)
  -  Orange for moderate scores (50-69)
  -  Red for poor scores (<50)
- **Skill Tags**: Missing skills highlighted in red, strengths in green
- **Responsive Design**: Beautiful gradients and smooth animations
- **Loading States**: Visual feedback during AI processing

## Architecture

ResuMentor follows a modern microservices architecture with clear separation of concerns:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit UI  │    │   FastAPI       │    │   AI Agents     │
│   (Frontend)    │◄──►│   (Backend)     │◄──►│   (Core Logic)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Components    │    │   API Routes    │    │   Utils &       │
│   - Screening   │    │   - /session    │    │   Parsers       │
│   - Learning    │    │   - /screen     │    │   - Resume      │
│   - Chat        │    │   - /plan       │    │   - YouTube     │
└─────────────────┘    │   - /chat       │    └─────────────────┘
                       └─────────────────┘
```

### System Components
- **Frontend**: Streamlit-based web interface with custom styling
- **Backend**: FastAPI REST API with CORS support
- **AI Agents**: Specialized agents for screening, learning path generation, and chat
- **Utilities**: Resume parsing (PDF/DOCX) and YouTube resource finder

## Technology Stack

### Backend Technologies
- **FastAPI** (0.104.0+) - Modern, fast web framework for building APIs
- **Uvicorn** (0.24.0+) - ASGI server for FastAPI
- **Pydantic** (2.5.0+) - Data validation and settings management
- **Python-multipart** - File upload handling

### AI & Machine Learning
- **OpenAI API** - Core AI capabilities
- **Agno** (0.1.0+) - Agent framework for AI interactions
- **DeepInfra** - Alternative AI model provider

### Frontend Technologies
- **Streamlit** (1.28.0+) - Rapid web app development
- **Custom CSS** - Enhanced UI styling and animations

### Document Processing
- **PyMuPDF** (1.23.0+) - PDF text extraction
- **Python-docx** (0.8.11+) - DOCX file processing

### Additional Dependencies
- **Requests** (2.31.0+) - HTTP client for API calls
- **Python-dotenv** (1.0.0+) - Environment variable management
- **FastAPI-CORS** (0.0.6+) - Cross-origin resource sharing

## Quick Start

### Prerequisites
- Python 3.11+
- DeepInfra API key
- YouTube API key (for learning path resources)

### Local Development Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd ResuMentor
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
Create a `.env` file in the root directory:
```env
DEEPINFRA_API_KEY=your_deepinfra_api_key
DEEPINFRA_MODEL=deepseek-ai/DeepSeek-V3.2-Exp
YOUTUBE_API_KEY=your_youtube_api_key
```

4. **Start the backend server**
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`

5. **Start the frontend application**
```bash
cd ui
streamlit run app.py
```
The web interface will be available at `http://localhost:8501`

### Docker Setup

1. **Using Docker Compose (Recommended)**
```bash
docker-compose up --build
```

2. **Using Docker directly**
```bash
docker build -t resumentor .
docker run -p 8000:8000 -e DEEPINFRA_API_KEY=your_key resumentor
```

## Usage Guide

### For Recruiters
1. **Upload Resume**: Upload candidate's resume in PDF or DOCX format
2. **Select Role**: Choose "I'm a recruiter"
3. **Enter Job Description**: Paste the complete job description and requirements
4. **Screen Resume**: Click "Screen Resume" to get AI analysis
5. **Review Results**: Analyze the fit score, strengths, and areas for improvement
6. **Make Decision**: Use insights to make informed hiring decisions

### For Job Seekers
1. **Upload Resume**: Upload your resume in PDF or DOCX format
2. **Select Role**: Choose "I'm applying for the job"
3. **Enter Job Description**: Paste the target job description
4. **Screen Resume**: Click "Screen Resume" to get AI analysis
5. **View Results**: See your fit score, strengths, and missing skills
6. **Generate Learning Path**: Click "Cover Up My Missing Skills" for personalized learning
7. **Chat with AI**: Ask questions about your learning path or career development

## Development

### Project Structure
```
ResuMentor/
├── agents/                 # AI agent implementations
│   ├── base.py            # Base agent class
│   ├── screener_agent.py  # Resume screening logic
│   ├── pathgenerator_agent.py # Learning path generation
│   └── chatbot_agent.py   # AI chat functionality
├── app/                   # FastAPI backend
│   ├── api/               # API route handlers
│   ├── main.py           # FastAPI app initialization
│   └── state.py           # Application state management
├── ui/                    # Streamlit frontend
│   ├── components/        # UI components
│   ├── app.py            # Main Streamlit app
│   └── api_client.py     # Backend API client
├── utils/                 # Utility functions
│   ├── resume_parser.py  # Document parsing
│   └── youtube_resource_finder.py # YouTube integration
├── prompts/              # AI prompts and templates
└── requirements.txt      # Python dependencies
```

### Adding New Features
1. **Backend**: Add new routes in `app/api/` and implement logic in `agents/`
2. **Frontend**: Create new components in `ui/components/` and integrate in `app.py`
3. **AI Agents**: Extend `BaseAgent` class for new AI functionality

### Environment Variables
Make sure these are set in your `.env` file:
```env
DEEPINFRA_API_KEY=your_api_key_here
DEEPINFRA_MODEL=deepseek-ai/DeepSeek-V3.2-Exp
YOUTUBE_API_KEY=your_youtube_api_key_here
```

### Logs and Debugging
- **Backend logs**: Check terminal where `uvicorn` is running
- **Frontend logs**: Check Streamlit logs in terminal
- **Docker logs**: `docker-compose logs resumentor-backend`


### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation for API changes
- Ensure all existing tests pass

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributors

- **Ansh Agnihotri** - Project Creator & Lead Developer
