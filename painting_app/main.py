from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from painting_app.models.models import User, Room
from typing import Dict, List
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Painting App")

ROOMS_DATABASE = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def home():
    return {"Message": "Welcome to Painting App!"}

# post /room # create room

@app.post("/room")
async def creat_room(room: Room):
    room.id = uuid4()
    ROOMS_DATABASE.append(room)
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