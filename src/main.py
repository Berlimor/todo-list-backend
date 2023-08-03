from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    message = {"message": "Hello World!"}
    return message