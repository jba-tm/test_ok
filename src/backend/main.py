from pydantic import BaseModel, Field
from fastapi import FastAPI, Body

app = FastAPI()


class UserIn(BaseModel):
    login: str = Field(
            ...,
            max_length=50,
            min_length=3,
            title='User login',
        description='Input your user login',
    )

    password: str = Field(
            ...,
            max_length=50,
            min_length=8,
            title='User password',
            password='Input you user password'
        )


@app.post("/ok/auth")
async def auth(
        user_in: UserIn = Body(
        ...,
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "login": "Foo",
                    "password": "secret-1",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "login": "Foo-3",
                    "password": "secret",
                },
            },
        },
    ),
):
    print(user_in)
    return {'status': 'ok', 'id': 123, 'name': 'xxx yyy'}
