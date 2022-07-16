from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def about():
    return 'Это мой курсовой проект. Я делаю стартап на Python/FastAPI. Покажу рекрутеру.'

# @app.get("/info")

# @app.get("/info/{person}")