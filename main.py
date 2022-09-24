from fastapi import FastAPI
import time

app = FastAPI()

@app.get('/')
def rota():
    time.sleep(12)
    return {"ola":"mundo!"}