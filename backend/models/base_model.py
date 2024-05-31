class BaseModel:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {key: getattr(self, key) for key in self.__dict__}

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

