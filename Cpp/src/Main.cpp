#include <iostream>
#include "BaseAdvertising.hpp"
#include "Advertiser.hpp"
#include "Ad.hpp"
using namespace std;


int main(){
    BaseAdvertising *base_advertising = new BaseAdvertising();
    Advertiser *advertiser1 = new Advertiser("name1");
    Advertiser *advertiser2 = new Advertiser("name2");
    Ad *ad1 = new Ad("title1", "img-url1", "link1", advertiser1);
    Ad *ad2 = new Ad("title2", "img-url2", "link2", advertiser2);

    cout << base_advertising->describe_me() << endl;
    cout << ad2->describe_me() << endl;
    cout << advertiser1->describe_me() << endl;

    ad1->inc_views();
    ad1->inc_views();
    ad1->inc_views();
    ad1->inc_views();
    ad2->inc_views();
    ad1->inc_clicks();
    ad1->inc_clicks();
    ad2->inc_clicks();

    cout << advertiser2->get_name() << endl;
    advertiser2->set_name("new name");
    cout << advertiser2->get_name() << endl;
    cout << ad1->get_clicks() << endl;
    cout << advertiser2->get_clicks() << endl;
    cout << Advertiser::get_total_clicks() << endl;
    cout << Advertiser::help() << endl;
}