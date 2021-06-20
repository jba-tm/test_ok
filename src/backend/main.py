from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/ok/auth")
async def auth(
        login: str = Query(
            ...,
            max_length=50,
            min_length=3,
            regex='',
            title='User login', description='Input your user login',

            examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "login": "login",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "login": "wrong_login",
                    },
                },
            },
        ),
        password: str = Query(
            ...,
            max_length=50,
            min_length=8,
            title='User password',
            password='Input you user password'
        )
):
    print({'login': login, 'password': password})
    return {'status': 'ok', 'id': 123, 'name': 'xxx yyy'}
