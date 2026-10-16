from pydantic import BaseModel, EmailStr, Field, ConfigDict
from fastapi import FastAPI

app = FastAPI()

data = {
    "email": "abc@mail.ru",
    "bio": "Я пирожок",
    "age": 12
}

data_wo_age = {
    "email": "abc@mail.ru",
    "bio": "Я пирожок",
   "gender": "male",
   "birthday": "2022"
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)

    model_config = ConfigDict(extra='forbid')


users = []

@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)


@app.get("/users")
def get_users():
    return users


class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)