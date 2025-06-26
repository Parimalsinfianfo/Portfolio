from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path
import uvicorn

app = FastAPI(
    title="Parimal Kulkarni Portfolio", 
    description="AI/ML Engineer Portfolio",
    version="1.0.0"
)

# Create templates directory if it doesn't exist
templates_dir = Path("templates")
templates_dir.mkdir(exist_ok=True)

# Create static directory if it doesn't exist
static_dir = Path("static")
static_dir.mkdir(exist_ok=True)

# Mount static files (for CSS, JS, images if you add them later)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates configuration
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the main portfolio page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy", 
        "message": "Portfolio server running",
        "version": "1.0.0"
    }

@app.get("/api/portfolio-info")
async def get_portfolio_info():
    """API endpoint to get portfolio information"""
    return {
        "name": "Parimal Kulkarni",
        "title": "AI/ML Engineer & Data Scientist", 
        "specializations": [
            "Generative AI",
            "Large Language Models (LLMs)", 
            "RAG Systems",
            "Machine Learning",
            "Data Science"
        ],
        "contact": {
            "email": "parimalhkulkarni2@gmail.com",
            "phone": "+91 8087768244",
            "location": "Pune, India",
            "github": "https://github.com/parimal1009",
            "linkedin": "https://www.linkedin.com/in/parimal-kulkarni-343877282/"
        }
    }

@app.get("/favicon.ico")
async def favicon():
    """Serve favicon"""
    return FileResponse("static/favicon.ico", media_type="image/x-icon")

# Error handlers
@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)

@app.exception_handler(500) 
async def server_error_handler(request: Request, exc):
    return templates.TemplateResponse("500.html", {"request": request}, status_code=500)

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True,
        log_level="info"
    )
