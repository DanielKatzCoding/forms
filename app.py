from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from router.questions.get_pages import router as dynamic_pages_router

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Include the dynamically created routes
app.include_router(dynamic_pages_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=80)
