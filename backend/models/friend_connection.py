from models.base_model import BaseModel

class FriendConnection(BaseModel):
    def __init__(self, user_id, friend_id):
        super().__init__(user_id=user_id, friend_id=friend_id)

