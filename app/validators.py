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
