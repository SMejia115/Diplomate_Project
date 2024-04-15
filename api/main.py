from fastapi import FastAPI
from routes.auth import auth_router


# Create FastAPI instance
app = FastAPI()
app.title = "Backend CapClocks"


app.include_router(auth_router)
