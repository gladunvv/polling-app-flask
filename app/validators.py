from pydantic import BaseModel, validator
from datetime import datetime
from typing import List
import json

class MessengerValidators(BaseModel):
    telegramm: bool
    whatsapp: bool
    viber: bool

class ContactValidators(BaseModel):
    user_name: str = None
    phone_number: int
    messanger: MessengerValidators

class MessageValidators(BaseModel):
    message: str
    date_at: datetime = None
    contact_list: List[ContactValidators]

    @validator('date_at', pre=True, always=True)
    def set_date_at_now(cls, date):
        return date or datetime.now()


def test_validators():
    mes = {
        "message": "Hello World!!!",
        "date_at": "2017-11-08 14:00",
        "contact_list": [
            {
            "user_name": "Vasya",
            "phone_number": 89990802112,
            "messanger":
                {
                "telegramm": True,
                "whatsapp": True,
                "viber": False
                }
            }
        ]
    }
    print(MessageValidators(**mes))
