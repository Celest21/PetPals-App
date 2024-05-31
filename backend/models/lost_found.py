from models.base_model import BaseModel

class LostFound(BaseModel):
    def __init__(self, user_id, pet_name, status, description, last_seen_location, contact_info, date_reported):
        super().__init__(user_id=user_id, pet_name=pet_name, status=status, description=description, last_seen_location=last_seen_location, contact_info=contact_info, date_reported=date_reported)
