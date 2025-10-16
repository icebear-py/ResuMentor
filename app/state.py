from datetime import datetime

sessions = {}
SESSION_TTL_SECONDS = 3600

def is_session_expired(session_id: str) -> bool:
    if session_id not in sessions:
        return True
    data = sessions[session_id]
    age = (datetime.utcnow() - data["created"]).total_seconds()
    return age > SESSION_TTL_SECONDS