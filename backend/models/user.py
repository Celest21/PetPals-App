from base_model import BaseModel

class User(BaseModel):
    def __init__(self, username, email, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.email = email

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
