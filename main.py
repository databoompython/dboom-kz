from fastapi import FastAPI

app = FastAPI()


my_db = {
    'Rawan': {
        'salary': '7500',
        'department': 'Development'
    },
    'Yuriy': {
        'salary': '3000',
        'department': 'Data analytics'
    },
    'Gulsim': {
        'salary': '3000',
        'department': 'Data analytics'
    }              
}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def about():
    return 'Это мой курсовой проект. Я делаю стартап на Python/FastAPI. Покажу рекрутеру.'

@app.get("/info")
def info():
    return my_db

@app.get("/info/{person}")
def get_personal_info(person):
    if person in my_db:
        return my_db[person]
    else:
        return 'К сожалению, нет такого пользователя, вы можете зарегистрироваться по этой ссылке - link'
