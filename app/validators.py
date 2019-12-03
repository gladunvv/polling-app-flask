from pydantic import BaseModel, ValidationError, validator
from datetime import datetime
from typing import List

class MessengerValidators(BaseModel):
    telegramm: bool
    whatsapp: bool
    viber: bool

class ContactValidators(BaseModel):
    user_name: str = None
    phone_number: int
    messanger: List[MessengerValidators]

class MessageValidators(BaseModel):
    message: str
    date_at: datetime = None
    contact_list: List[ContactValidators]

    @validator('date_at', pre=True, always=True)
    def set_date_at_now(cls, date):
        return date or datetime.now()

    @validator('date_at', pre=True, always=True)
    def date_before_now(cls, date):
        date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        if date.date() < datetime.now().date():
            raise ValueError('Date must be after now')
        return date

def test():
    mes = {
        "message": "Hello World!!!",
        "date_at": "2017-11-08 14:00",
        "contact_list": [
            {
                "user_name": "Vasya",
                "phone_number": 89990802112,
                "messanger": [
                    {
                    "telegramm": True,
                    "whatsapp": True,
                    "viber": False
                    },
                ]
            },
        ]
    }

    print(MessageValidators(**mes))