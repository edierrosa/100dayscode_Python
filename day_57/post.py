class Post:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    # def __init__(self, **kwargs):
    #     for k, v in kwargs.items():
    #         setattr(self, k, v)
