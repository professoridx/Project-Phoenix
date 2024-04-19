from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    password: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    
    class Config:
         from_attributes=True


        
        

