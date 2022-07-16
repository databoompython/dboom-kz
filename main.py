from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/about")

# @app.get("/info")

# @app.get("/info/{person}")