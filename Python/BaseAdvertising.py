
class BaseAdvertising:
    """base class that tracks views and clicks"""
    def __init__(self):
        self.__clicks = 0
        self.__views = 0

    def get_clicks(self):
        return self.__clicks

    def get_views(self):
        return self.__views

    def inc_clicks(self):
        self.__clicks += 1

    def inc_views(self):
        self.__views += 1

    def describe_me(self):
        return self.__doc__
