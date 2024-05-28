from router.questions.get_pages import router as dynamic_pages_router
from router.dump_form_data import router as dump_form_router
from fastapi import FastAPI, Request, Form
import uvicorn

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

# Include the dynamically created routes
app.include_router(dynamic_pages_router)
app.include_router(dump_form_router)

if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=80)
