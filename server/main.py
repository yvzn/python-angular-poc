"""Module providing API endpoints."""

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()





# -- Static files ---------------------------------------------------

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(_: Request):
    """Serve index.html file at the root path."""
    file_name = 'index.html'
    file_path = './static/' + file_name
    return FileResponse(file_path)

@app.get('/favicon.ico')
async def favicon():
    """Serve favicon.ico"""
    file_name = 'favicon.ico'
    file_path = './static/' + file_name
    return FileResponse(path=file_path, headers={'mimetype': 'image/vnd.microsoft.icon'})

@app.middleware("http")
async def spa_routing(request: Request, call_next):
    """SPA routing middleware to serve index.html for any non-API path."""
    response = await call_next(request)
    if response.status_code == 404 and not request.url.path.startswith("/api"):
        file_name = 'index.html'
        file_path = './static/' + file_name
        return HTMLResponse(file_path)
    return response





# -- API endpoints --------------------------------------------------

@app.get("/api/about")
def about():
    """About page information."""
    return {"Hello": "World"}





# -- Main ------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
