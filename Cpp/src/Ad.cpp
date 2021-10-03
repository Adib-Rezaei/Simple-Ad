#include <string>
#include "Ad.hpp"
using namespace std;

int Ad::id_counter;

Ad::Ad(std::string title, std::string img_url, std::string link, Advertiser *advertiser){
    this->title = title;
    this->img_url = img_url;
    this->link = link;
    this->advertiser = advertiser;
    this->id = ++Ad::id_counter;
}

std::string Ad::get_title(){
    return title;
}

void Ad::set_title(std::string title){
    this->title = title;
}

std::string Ad::get_img_url(){
    return img_url;
}

void Ad::set_img_url(std::string img_url){
    this->img_url = img_url;
}

std::string Ad::get_link(){
    return link;
}

void Ad::set_link(std::string link){
    this->link = link;
}

void Ad::set_advertiser(Advertiser *advertiser){
    this->advertiser = advertiser;
}

void Ad::inc_clicks(){
    advertiser->inc_clicks();
    BaseAdvertising::inc_clicks();
}

void Ad::inc_views(){
    advertiser->inc_views();
    BaseAdvertising::inc_views();
}

std::string Ad::describe_me(){
    return "Ad class represents an ad that is owned by an advertiser";
}
