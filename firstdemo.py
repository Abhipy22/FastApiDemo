from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def sample():
    return {"test":"data"}

@app.get("/retest")
def retest(int):
    
    return {"name":"ansh"}

        