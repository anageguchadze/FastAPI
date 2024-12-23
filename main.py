from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def test_function():
    return {'Message': 'Hello'}