from fastapi import FastAPI

app = FastAPI()


@app.get("/")

def index():

    return{"name":"hello"}

@app.get("/About")

def about():
    return{"hobbies":"playing cricket"}
    




