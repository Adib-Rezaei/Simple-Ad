#ifndef AD_HPP
#define AD_HPP
#include <string>
#include "BaseAdvertising.hpp"
#include "Advertiser.hpp"

class Ad : public BaseAdvertising {
public:
    Ad(std::string title, std::string img_url, std::string link, Advertiser *advertiser);
    std::string get_title();
    void set_title(std::string title);
    std::string get_img_url();
    void set_img_url(std::string img_url);
    std::string get_link();
    void set_link(std::string link);
    void set_advertiser(Advertiser *advertiser);
    void inc_clicks();
    void inc_views();
    std::string describe_me();

private:
    static int id_counter;
    std::string title;
    std::string img_url;
    std::string link;
    Advertiser* advertiser;

};

#endif