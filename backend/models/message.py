from models.base_model import BaseModel

class Message(BaseModel):
    def __init__(self, sender_id, recipient_id, content, timestamp):
        super().__init__(sender_id=sender_id, recipient_id=recipient_id, content=content, timestamp=timestamp)
