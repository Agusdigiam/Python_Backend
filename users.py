from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    email: str
    age: int

Users_list = [
User(name="Agustin", surname="Di Giambatista",email="agus@gmail.com",age=28),
User(name="Gian",surname="Vespa", email="Gian_Vespa@user.com", age=30 ),
User(name="Daniel",surname= "Massara", email="Massara@user.com", age=43)]


@app.get("/usersclass")
async def usersclass():
    return Users_list



@app.get("/users")
async def user():
    return [{"name" :"Agustin",
            "surname" : "Di Giambatista",
            "email" : "agus@user.com",
            "age" : "28",
            },
            {"name" :"Gian",
            "surname" :"Vespa",
            "email" : "Gian_Vespa@user.com",
            "age" : "30",
            },
            {"name" :"Daniel",
            "surname" : "Massara",
            "email" : "Massara@user.com",
            "age" : "43",
            },
            ]

