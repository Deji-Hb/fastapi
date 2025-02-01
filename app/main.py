#command to create a virtual environment is py -3 -m venv <name>
import os 
import uvicorn
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from pydantic_settings import BaseSettings
from fastapi.middleware.cors import CORSMiddleware

#we don't need this  for some reason since we're using alembic 
#models.Base.metadata.create_all(bind=engine)


app = FastAPI()

#origins = ["https://www.google.com", "https://www.youtube.com"]

#to set the api to talk to every domain e.g to set a public api
origins = ["*"]

#to allow our api to communicate with other domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# path operation or route
# @app is the decorator, get is the http method, "/" is the root path which is the path we have to go to when typing the url
# the order of retrieving data from get method matters first one will be passed first
@app.get("/")
def root():
    return {"message": "Hello Deji"}


# def add(num1, num2):
#     return (num1 + num2)
# def subtract(num1, num2):
#     return (num1 - num2)
# def multiply(num1, num2):
#     return (num1 * num2)

# def Calculator(action, num1, num2):
#     if action == "add":
#         return add(num1=num1, num2=num2)
#     if action == "subtract":
#         return subtract(num1=num1, num2=num2)
#     if action == "multiply":
#         return multiply(num1=num1, num2=num2)


# @app.get("/cal")
# def mehhh(
#     action: str, num1: int, num2: int
# ):
#     ans = Calculator(action=action, num1=num1, num2=num2)
#     return f"Suck mah ballz, the answer is {ans}"

if __name__ == "__main__":
    # Retrieve the port from environment variables or default to 8000
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)