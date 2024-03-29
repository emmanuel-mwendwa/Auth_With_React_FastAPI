from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

# from .database import engine

from .routers import user, auth, leads


# from . import models

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(leads.router)


@app.get("/")
async def home():
    return {"message": "Welcome to my react auth application"}