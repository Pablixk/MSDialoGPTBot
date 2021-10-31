from fastapi import FastAPI
import uvicorn
import bot_service as bot
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    user_uid: str
    message: str


# Send post message to bot
@app.post("/bot/message/")
def get_message(message: Message) -> dict:
    response = bot.get_message(message.message, message.user_uid)
    return {"response": response}


# Start uvicorn web server con host 127.0.0.1 and port 5000
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
