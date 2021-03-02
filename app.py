import secrets

from fastapi import Depends, FastAPI, HTTPException, status, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

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


@app.get("/", response_class=HTMLResponse)
def index(request:Request, username: str = Depends(get_current_username)):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/info/")
async def findout(request: Request, url: str, location: str, username: str = Depends(get_current_username)):
    return templates.TemplateResponse("response.html", {'request': request, 'url': url, 'location': location})
