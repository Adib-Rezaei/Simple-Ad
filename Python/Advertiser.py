from BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    """keeps track of advertiser information and his ad stats"""
    id_counter: int = 1
    total_clicks: int = 0
    
    def __init__(self, name):
        super().__init__()
        self.__name = name 
        self.__id = Advertiser.id_counter
        Advertiser.id_counter += 1

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def inc_clicks(self):
        Advertiser.total_clicks += 1
        super().inc_clicks()

    @staticmethod
    def help():
        return 'This class has some fields' + \
            "get_name(): return name\n" + \
            "set_name(): sets new name\n" + \
            "inc_clicks(): increment Advertiser and Total clicks by 1\n" + \
            "inc_views(): increment Advertiser views by 1\n" + \
            "get_clicks(): return number of clicks on all ads\n" + \
            "get_views(): return number of views on all ads\n" + \
            "get_total_clicks(): total Advertisers clicks\n" + \
            "describe_me(): short description of class"

    def describe_me(self):
        return self.__doc__

    @staticmethod
    def get_total_clicks():
        return Advertiser.total_clicks


