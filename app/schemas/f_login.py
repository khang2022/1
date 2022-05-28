from pydantic import BaseModel
#1

class LoginForm (BaseModel):
   
    email : str
    password : str
   
     