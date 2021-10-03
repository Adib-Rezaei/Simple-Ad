from BaseAdvertising import BaseAdvertising


class Ad(BaseAdvertising):
    """represents an ad that is owned by an advertiser"""
    id_counter: int = 1

    def __init__(self, title, img_url, link, advertiser):
        super().__init__()
        self.__id = Ad.id_counter
        self.__title = title 
        self.__img_url = img_url
        self.__link = link 
        self.__advertiser = advertiser
        Ad.id_counter += 1

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_img_url(self):
        return self.__img_url
    
    def set_img_url(self, img):
        self.__img_url = img

    def get_link(self):
        return self.__link

    def set_link(self, link):
        self.__link = link 

    def set_advertiser(self, advertiser):
        self.__advertiser = advertiser

    def inc_clicks(self):
        super().inc_clicks()
        self.__advertiser.inc_clicks()

    def inc_views(self):
        super().inc_views()
        self.__advertiser.inc_views()

    def describe_me(self):
        return self.__doc__
