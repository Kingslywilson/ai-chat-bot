from pathlib import Path
import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from groq import Groq

BASE_DIR = Path(__file__).parent

load_dotenv(BASE_DIR.parent / ".env")

app = FastAPI(title="College Course Advisor Bot")

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

with open(
    BASE_DIR / "system_prompt.txt",
    "r",
    encoding="utf-8"
) as f:
    SYSTEM_PROMPT = f.read()


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)


class ChatResponse(BaseModel):
    response: str


conversation_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    message = request.message.strip()

    if not message:
        raise ValueError("Message cannot be empty.")

    conversation_history.append(
        {
            "role": "user",
            "content": message
        }
    )

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=conversation_history
    )

    assistant_response = completion.choices[0].message.content

    conversation_history.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )

    return ChatResponse(response=assistant_response)