from fastapi import FastAPI
from api import employee as emp
from fastapi.responses import RedirectResponse

app = FastAPI()

app.include_router(emp.router)

@app.get("/")
def root():
    return RedirectResponse(url="/docs")