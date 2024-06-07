from models.base_model import BaseModel

class LostFound(BaseModel):
    def __init__(self, user_id, pet_name, description, lost_date, contact_info):
        super().__init__(user_id=user_id, pet_name=pet_name, description=description, lost_date=lost_date, contact_info=contact_info)
