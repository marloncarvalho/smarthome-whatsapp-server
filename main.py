from fastapi import FastAPI
from alright import WhatsApp
from pydantic import BaseModel

app = FastAPI()
whatsapp = WhatsApp()

class Message(BaseModel):
    user: str
    text: str

@app.post("/whatsapp/messages")
async def send_message(message: Message):
    whatsapp.find_user(message.user)
    whatsapp.send_message(message.text)

    return {"status": "OK"}



