from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello world"}

@app.get("/about")
def home():
    return {"message": "This is a test fastapi project."}