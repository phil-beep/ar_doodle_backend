from fastapi import HTTPException, status
from fastapi.security import HTTPBasicCredentials
from creds import username, password
import secrets

def validate(credentials: HTTPBasicCredentials):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = bytes(username, "utf-8")
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = bytes(password, "utf-8")
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nope",
            headers={"WWW-Authenticate": "Basic"},
        )