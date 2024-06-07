from models.base_model import BaseModel

class Comment(BaseModel):
    def __init__(self, user_id, post_id, content, timestamp):
        super().__init__(user_id=user_id, post_id=post_id, content=content, timestamp=timestamp)
