from models.base_model import BaseModel

class Media(BaseModel):
    def __init__(self, user_id, media_type, url, description, timestamp):
        super().__init__(user_id=user_id, media_type=media_type, url=url, description=description, timestamp=timestamp)

