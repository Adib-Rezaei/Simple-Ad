from BaseAdvertising import BaseAdvertising
from Advertiser import Advertiser
from Ad import Ad


if __name__ == '__main__':
    baseAdvertising = BaseAdvertising()
    advertiser1 = Advertiser('name1')
    advertiser2 = Advertiser('name2')

    ad1 = Ad('title1', 'img1', 'link1', advertiser1)
    ad2 = Ad('title2', 'img2', 'link2', advertiser2)

    print(baseAdvertising.describe_me())
    print(ad2.describe_me())
    print(advertiser1.describe_me())

    ad1.inc_views()
    ad1.inc_views()
    ad1.inc_views()
    ad1.inc_views()
    ad2.inc_views()
    ad1.inc_clicks()
    ad1.inc_clicks()
    ad2.inc_clicks()
    print(advertiser2.get_name())
    advertiser2.set_name('new name')
    print(advertiser2.get_name())
    print(ad1.get_clicks())
    print(advertiser2.get_clicks())
    print(Advertiser.get_total_clicks())
    print(Advertiser.help())
