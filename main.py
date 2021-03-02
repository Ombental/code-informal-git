import secrets

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "NoalOnly")
    correct_password = secrets.compare_digest(credentials.password, "NOAL19241948")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/")
def home(username: str = Depends(get_current_username)):
    return {"username": username}

@app.get("/info/")
async def findout(url: str, location: str, username: str = Depends(get_current_username)):
    return {'url': url, 'location': location}
