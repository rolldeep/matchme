from pydantic import BaseModel
from datetime import datetime

from fastapi import FastAPI

class Transfer(BaseModel):
    user_from: str
    currency_pair: str | None = None
    amount: float
    transfer_datetime: datetime


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/create_transfer")
def create_transfer_request(transfer: Transfer):
    return transfer 