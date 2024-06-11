import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from router.get_pages import router as dynamic_pages_router
from utils.form_handle import router as form_handle_router

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

# Include the dynamically created routes
app.include_router(dynamic_pages_router)
app.include_router(form_handle_router)

if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=8001)
