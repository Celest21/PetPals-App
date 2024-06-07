from models.base_model import BaseModel

class Pet(BaseModel):
    def __init__(self, name, species, breed, age, owner_id, description=None, gender=None, photos=None, health_info=None):
        super().__init__(name=name, species=species, breed=breed, age=age, owner_id=owner_id, description=description, gender=gender, photos=photos, health_info=health_info)
