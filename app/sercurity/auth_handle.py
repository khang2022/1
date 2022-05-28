import time
import jwt
from decouple import config
from typing import Dict


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return {
        "access_token": token
    }

#1
def encodeJWT(user_email: str,role : str,id : int) -> Dict[str, str]:
    
    payload = {
        "user_email": user_email,
        "role"   : role,
        "expires": time.time() + 600,
        "id"     : id
    }
 
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)




def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}


