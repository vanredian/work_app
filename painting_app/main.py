from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from painting_app.models.models import User, Room
from typing import Dict, List
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os
import json
from fastapi.encoders import jsonable_encoder

app = FastAPI(title="Painting App")


ROOMS_FILE = "rooms.json"
ROOMS_DATABASE = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if os.path.exists(ROOMS_FILE):
    with open(ROOMS_FILE, "r") as f:
        ROOMS_DATABASE = json.load(f)

@app.get("/")
async def home():
    return {"Message": "Welcome to Painting App!"}

# post /room # create room

@app.post("/room")
async def create_room(room: Room):
    room.id = uuid4()
    room.last_activity = datetime.now()
    json_room = jsonable_encoder(room)
    ROOMS_DATABASE.append(json_room)
    with open(ROOMS_FILE, "w") as f:
        json.dump(ROOMS_DATABASE, f, indent=4)
    return {"Message": "Room has been added"}



# post /room/{room_id} # Join to room


@app.post("/room/{room_id}")
async def join_room(room_id: UUID):
    for room in ROOMS_DATABASE:
        if room_id == room.id:
            return {"Room info": room}       
    raise HTTPException(404, f"Room {room_id} is not found.")




# get /rooms # List rooms

@app.get("/rooms")
async def rooms():
    return {"Room list": ROOMS_DATABASE}


# get /rooms/{room_id} # Details of {room_id}

@app.get("/rooms/{room_id}")
async def get_room(room_id: UUID):
    for room in ROOMS_DATABASE:
        if room_id == room.id:
            return {"Room info": room}
        
    raise HTTPException(404, f"Room {room_id} is not found.")

# post /room/{room_id}/user/{user_id}/push
# get /room/{room_id}/user/{user_id}/pull 