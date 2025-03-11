import uvicorn
from fastapi import FastAPI

from src.chat import router as chatRouter
from src.dashboard import router as dashboardRouter
from src.header import router as headerRouter
from src.project import router as projectRouter

app = FastAPI()
app.include_router(headerRouter)
app.include_router(dashboardRouter)
app.include_router(chatRouter)
app.include_router(projectRouter)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
