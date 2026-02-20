from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

posts: list[dict] = [
    {
        "id": 1,
        "author": "Ishaan Agarwal",
        "title": "First Test 1",
        "content": "This is a test blog for my fast api app",
        "date_posted": "March 22, 2025",
    },
    {
        "id": 2,
        "author": "Adveet Agarwal",
        "title": "First Test 2",
        "content": "This is a second blog for my fast api app",
        "date_posted": "Feb 18, 2026",
    },

]


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", 
        {"posts": posts, "title":"Home"},
        )


@app.get("/api/posts")
def get_posts():
    return posts 