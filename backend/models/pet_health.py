from models.base_model import BaseModel

class PetHealth(BaseModel):
    def __init__(self, user_id, pet_name, health_info, timestamp):
        super().__init__(user_id=user_id, pet_name=pet_name, health_info=health_info, timestamp=timestamp)
