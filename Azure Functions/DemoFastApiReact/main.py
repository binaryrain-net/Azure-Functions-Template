from os.path import abspath, dirname
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import logging
import random


logger = logging.getLogger(__name__)

app = FastAPI()

# CORS config (adjust in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates & Static
dist_dir = f"{dirname(abspath(__file__))}/frontend/dist"
# Serve static assets (JS/CSS) under /assets
app.mount("/assets", StaticFiles(directory=f"{dist_dir}/assets"), name="assets")


# Root route serves the built index.html
@app.get("/", response_class=HTMLResponse)
async def home():
    return FileResponse(f"{dist_dir}/index.html")


@app.get("/api/get-random-number", response_class=JSONResponse)
def get_random_number() -> JSONResponse:
    logger.info("Get random number request received.")
    random_number = random.randint(1, 100)
    logger.info(f"Generated random number: {random_number}")
    return JSONResponse(content={"randomNumber": random_number})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
