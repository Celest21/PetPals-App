from models.base_model import BaseModel

class UserProfile(BaseModel):
    def __init__(self, user_id, bio, location, profile_pic):
        super().__init__(user_id=user_id, bio=bio, location=location, profile_pic=profile_pic)

