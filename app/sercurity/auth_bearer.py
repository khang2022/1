from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth_handle import decodeJWT


class JWTBearer(HTTPBearer):
    def __init__(self, role_list: list = None, auto_error: bool = True):
        super().__init__(auto_error=auto_error)
        self.role_list = role_list or []

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme.")
            payload = self.verify_jwt(credentials.credentials)
            if not payload:
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid = False
        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            for position in self.role_list:  # check role with roles were given
                if payload["role"] == position:
                      isTokenValid = True
                    # id = payload["id"]
                      break

        return isTokenValid
        # return payload
#1