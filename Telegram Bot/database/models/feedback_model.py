from pydantic import BaseModel

from ..loader import collection
from datetime import datetime


class Feedback(BaseModel):
    _id: int
    userName: str
    name: str
    message: str
    date: datetime
   


feedbacks_collection = collection.feedback