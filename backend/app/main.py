from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine

from .routers import transactions
from .routers import logins
from .routers import dashboard


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="BankGuard AI",
    description="Banking Security Monitoring Platform",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://192.168.29.89:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


app.include_router(
    transactions.router
)

app.include_router(
    logins.router
)

app.include_router(
    dashboard.router
)


@app.get("/")
def home():

    return {
        "message": "BankGuard AI API running"
    }