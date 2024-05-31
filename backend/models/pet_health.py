from models.base_model import BaseModel

class PetHealth(BaseModel):
    def __init__(self, user_id, pet_name, health_type, description, date, reminder=None):
        super().__init__(user_id=user_id, pet_name=pet_name, health_type=health_type, description=description, date=date, reminder=reminder)
