from models.base_model import BaseModel

class Recommendation(BaseModel):
    def __init__(self, user_id, pet_id, recommendation_type, recommendation_text):
        super().__init__(user_id=user_id, pet_id=pet_id, recommendation_type=recommendation_type, recommendation_text=recommendation_text)

