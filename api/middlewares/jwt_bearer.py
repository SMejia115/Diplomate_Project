from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from utils.jwt_manager import decode_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = decode_token(auth.credentials)
        if data['email'] != "admin@mail.com":
            raise HTTPException(status_code=401, 
                                detail="Invalid user")