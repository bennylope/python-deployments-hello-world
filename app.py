"""
Application definition
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def home():
    return HTMLResponse("Hello world!")


@app.get("/404")
async def missing():
    return HTMLResponse("That's gonna be a 'no' from me.", status_code=404)
