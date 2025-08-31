from typing import Union, Optional

from fastapi import FastAPI
import os
from livekit import api

from dotenv import load_dotenv
load_dotenv()
app = FastAPI(
    title = "MyRide Wallet Voice Assistant"
)


@app.get("/")
def health_check():
    return {"status": "API Working ..."}


@app.post("/getToken")
def getToken(auth_key: str, username: str):
  token = api.AccessToken(os.getenv('LIVEKIT_API_KEY'),
                        os.getenv('LIVEKIT_API_SECRET')) \
    .with_identity("uuid6589") \
    .with_name("MyRideWallet User") \
    .with_attributes({
        "auth_key": auth_key,
        "username": username
    }) \
    .with_grants(api.VideoGrants(
        room_join=True,
        room="room"
    ))
  return token.to_jwt()
