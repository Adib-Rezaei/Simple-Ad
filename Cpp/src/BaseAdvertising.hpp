#ifndef BASEADVERTISING_HPP
#define BASEADVERTISING_HPP
#include <string>

class BaseAdvertising {
public:

    BaseAdvertising() : clicks(0), views(0){};
    std::string describe_me();
    int get_clicks();
    int get_views();
    void inc_clicks();
    void inc_views();

protected:
    int id;

private:
    int clicks;
    int views; 

};


#endif