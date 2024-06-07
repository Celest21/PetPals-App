class BaseModel:
    def __init__(self, **kwargs):
        self._id = kwargs.get('_id', None)  # Initialize _id to None by default
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_')}  # Exclude attributes starting with _

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

