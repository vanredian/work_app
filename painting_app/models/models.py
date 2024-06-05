from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Dict, List

class Room(BaseModel):
    id: UUID
    name: str
    # participants: List[str] = []

class User(BaseModel):
    id: UUID