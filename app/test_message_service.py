import unittest
from app.validators import MessageValidators


class TestMessageService(unittest.TestCase):

    def test_validators(self):
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
        self.assertTrue(MessageValidators(**mes))
