from schemas.schemas import UsersBase
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token

auth_router = APIRouter()

@auth_router.post("/login", tags=["Auth"], response_model = dict, status_code=200)
def login(user: UsersBase):
    if user.email == "admin@mail.com" and user.password == "admin" and user.role == "admin":
        token = create_token(data=user.model_dump())
        result = JSONResponse(content={"token":token, "message": "Login successfully"}, status_code=200)
    else:
        result = JSONResponse(content={"message": "Invalid credentials"}, status_code=401)
    return result