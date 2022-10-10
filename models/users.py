from dataclasses import field
import email
from enum import unique
from uuid import UUID, uuid4
from beanie import Document , Indexed
from pydantic import Field , EmailStr


class USer(Document):
    user_id : UUID = Field(default_factory=uuid4 , unique=True)
    username : str = Indexed(str , unique=True)
    email : str = Field(unique=True)
    hashed_password : str

    super_user : bool = Field(default=False)

    class Collection:
        name = "users"