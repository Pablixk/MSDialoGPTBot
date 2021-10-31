# Chat Bot REST Server
<a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/python-v3.9-blue" alt="Supported Python versions">
</a>
<a href="https://huggingface.co" target="_blank">
    <img src="https://img.shields.io/badge/transformers-v4.12.0-green" alt="Supported Python versions">
</a>
<a href="https://pytorch.org/" target="_blank">
    <img src="https://img.shields.io/badge/PyTorch-v1.10.0-green" alt="Supported Python versions">
</a>
<a href="https://fastapi.tiangolo.com/" target="_blank">
    <img src="https://img.shields.io/badge/fastapi-v0.70.0-green" alt="Supported Python versions">
</a>
<a href="https://www.uvicorn.org/" target="_blank">
    <img src="https://img.shields.io/badge/uvicorn-v0.15.0-green" alt="Supported Python versions">
</a>
<a href="https://pydantic-docs.helpmanual.io/" target="_blank">
    <img src="https://img.shields.io/badge/pydantic-v1.8.2-green" alt="Supported Python versions">
</a>

HTTP REST Chat Bot on A State-of-the-Art Large-scale Pretrained Response generation model ([DialoGPT](https://huggingface.co/microsoft/DialoGPT-medium))  
### Describe
DialoGPT is a SOTA large-scale pretrained dialogue response generation model for multiturn conversations. The human evaluation results indicate that the response generated from DialoGPT is comparable to human response quality under a single-turn conversation Turing test. The model is trained on 147M multi-turn dialogue from Reddit discussion thread.

Server default start host 127.0.0.1 and port 5000
#### Attention 
At the first launch, the 1,34 GB model will be downloaded.
#### Server:

Endpoint bot message:
```python
class Message(BaseModel):
    user_uid: str
    message: str

# Send post message to bot
@app.post("bot/message/")
def get_message(message: Message):
    response = bot.get_message(message.message, message.user_uid)
    return {"response": response}
```
**message** - user text message
**user_uid** - unique user id (for chat history)

#### Example
POST message:
```json
{
  "user_uid": "123456",
  "message": "How are you?"
}
```
Response:
```json
{
  "response": "I'm good, how are you?"
}
```