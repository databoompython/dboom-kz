from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def about():
    return 'Это мой курсовой проект. Я делаю стартап на Python/FastAPI. Покажу рекрутеру.'

@app.get("/info")
def info():
    return {
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

# @app.get("/info/{person}")