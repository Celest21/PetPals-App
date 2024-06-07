from models.base_model import BaseModel

class Message(BaseModel):
    def __init__(self, sender_id, receiver_id, content, timestamp):
        super().__init__(sender_id=sender_id, receiver_id=receiver_id, content=content, timestamp=timestamp)

