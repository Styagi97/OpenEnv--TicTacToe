from fastapi import FastAPI
from models import MoveAction
from environment import TicTacToeEnv

app = FastAPI()
env = TicTacToeEnv()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: MoveAction):
    return env.step(action)


@app.get("/state")
def state():
    return env.state()

@app.get("/")
def home():
    return {"message" : "TicTacToeEnv API is running"}
