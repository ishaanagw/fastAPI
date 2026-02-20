from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[1]['title']}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts 