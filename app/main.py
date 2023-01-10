import uvicorn
from fastapi import FastAPI
from app.config import db


def init_app():
    db.init()
    
    app = FastAPI(
        title="My API",
        description="This is my API",
        version=1
    )
    @app.on_event("startup")
    async def startup():
        await db.create_all()
    
    @app.on_event("shutdown")
    async def shutdown():
        await db.close()
    
    return app



app = init_app()

def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
