from models.base_model import BaseModel

class Forum(BaseModel):
    def __init__(self, title, description):
        super().__init__(title=title, description=description)

class Thread(BaseModel):
    def __init__(self, forum_id, title, user_id, content, timestamp):
        super().__init__(forum_id=forum_id, title=title, user_id=user_id, content=content, timestamp=timestamp)

class Post(BaseModel):
    def __init__(self, thread_id, user_id, content, timestamp):
        super().__init__(thread_id=thread_id, user_id=user_id, content=content, timestamp=timestamp)
