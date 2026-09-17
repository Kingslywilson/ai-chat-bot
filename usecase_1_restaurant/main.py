import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from groq import Groq
from pydantic import BaseModel, Field
from fastapi.staticfiles import StaticFiles

load_dotenv()

app = FastAPI(title="Restaurant Ordering Bot")
BASE_DIR = Path(__file__).parent

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)

templates = Jinja2Templates(
    directory=str(Path(__file__).parent / "templates")
)

SYSTEM_PROMPT = (
    Path(__file__).parent / "system_prompt.txt"
).read_text(encoding="utf-8")


api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("GROQ_API_KEY is not configured.")

client = Groq(api_key=api_key)


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=2000
    )


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
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty."
        )

    conversation_history.append(
        {
            "role": "user",
            "content": message
        }
    )

    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=conversation_history,
            temperature=0.2,
            max_tokens=500,
        )

        response = completion.choices[0].message.content.strip()

    except Exception as exc:
        conversation_history.pop()

        raise HTTPException(
            status_code=502,
            detail="Unable to contact the language model."
        ) from exc

    conversation_history.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    return ChatResponse(response=response)