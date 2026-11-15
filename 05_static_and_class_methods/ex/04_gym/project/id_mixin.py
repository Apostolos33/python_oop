class IDMixin:
    id = 1

    @classmethod
    def get_next_id(cls):
        return cls.id

    @classmethod
    def increment(cls):
        cls.id += 1
