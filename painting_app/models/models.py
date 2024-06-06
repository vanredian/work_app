from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Dict, List
from datetime import datetime



class Room(BaseModel):
    id: UUID
    name: str
    # participants: List[str] = []
    last_activity: datetime = datetime.now()

class User(BaseModel):
    id: UUID