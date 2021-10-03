#ifndef ADVERTISER_HPP
#define ADVERTISER_HPP
#include <string>
#include "BaseAdvertising.hpp"

class Advertiser : public BaseAdvertising {
public:
    Advertiser(std::string name);
    std::string get_name();
    void set_name(std::string name);
    void inc_clicks();
    std::string describe_me();

    static std::string help();
    static int get_total_clicks();

private:
    std::string name;
    static int id_counter;
    static int total_clicks;

};

#endif