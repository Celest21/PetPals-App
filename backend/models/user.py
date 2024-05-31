from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, username, password, email=None):
        super().__init__(username=username, password=password, email=email)

