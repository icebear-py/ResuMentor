from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import session, screen, path, chat

app = FastAPI(title="ResuMentor API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(session.router, prefix="/session", tags=["Session"])
app.include_router(screen.router, prefix="/screen", tags=["Screening"])
app.include_router(path.router, prefix="/plan", tags=["Learning Plan"])
app.include_router(chat.router, prefix="/chat", tags=["Chat Tutor"])

@app.get("/")
def root():
    return {'message':'ResuMentor is live sir...'}