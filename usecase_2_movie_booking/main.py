from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from groq import Groq
import os


BASE_DIR = Path(__file__).parent

load_dotenv(BASE_DIR.parent / ".env")

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


with open(BASE_DIR / "system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


conversation_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        description="User message"
    )


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/chat")
async def chat(request: ChatRequest):

    message = request.message.strip()

    if not message:
        return {
            "error": "Message cannot be empty."
        }

    conversation_history.append(
        {
            "role": "user",
            "content": message
        }
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=conversation_history
    )

    assistant_message = response.choices[0].message.content

    conversation_history.append(
        {
            "role": "assistant",
            "content": assistant_message
        }
    )

    return {
        "response": assistant_message
    }