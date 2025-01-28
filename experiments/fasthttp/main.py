from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, magic!"}

def clean(a, b):
	print(f"You supplied {a} and {b}")

clean("cool", "been")
