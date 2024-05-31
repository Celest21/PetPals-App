from models.base_model import BaseModel

class UserProfile(BaseModel):
    def __init__(self, user_id, name, bio=None, profile_picture=None, location=None, social_links=None):
        super().__init__(user_id=user_id, name=name, bio=bio, profile_picture=profile_picture, location=location, social_links=social_links)
from models.base_model import BaseModel

class UserProfile(BaseModel):
    def __init__(self, user_id, name, bio=None, profile_picture=None, location=None, social_links=None):
        super().__init__(user_id=user_id, name=name, bio=bio, profile_picture=profile_picture, location=location, social_links=social_links)

