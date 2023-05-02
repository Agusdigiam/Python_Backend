from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int

Users_list = [
User(id= 1 , name="Agustin", surname="Di Giambatista",email="agus@gmail.com",age=28),
User(id= 2 , name="Gian",surname="Vespa", email="Gian_Vespa@user.com", age=30 ),
User(id= 3 , name="Daniel",surname= "Massara", email="Massara@user.com", age=43)]


#Hay dos metodos fundamentales: 


#Metodo Path:
@app.get("/user/{id}")
async def user(id: int):
        users = filter(lambda user: user.id == id, Users_list)
        try:
                return list(users)[0]
        except:
                return [{"error_EN": "The User don't exits"},
                        {"error_ES": "El Usuario que buscaste no existe"},]
        

#Metodo Query:
@app.get("/userquey/")
async def user(id: int):
        users = filter(lambda user: user.id == id, Users_list)
        try:
                return list(users)[0]
        except:
                return [{"error_EN": "The User don't exits"},
                        {"error_ES": "El Usuario que buscaste no existe"},]
                




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

