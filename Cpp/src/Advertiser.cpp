#include <iostream>
#include <string>
#include <sstream>
#include "BaseAdvertising.hpp"
#include "Advertiser.hpp"
using namespace std;

int Advertiser::id_counter;
int Advertiser::total_clicks;

Advertiser::Advertiser(string name){
    this->id = ++Advertiser::id_counter;
    this->name = name;
}

string Advertiser::get_name(){
    return name;
}

void Advertiser::set_name(string name){
    this->name = name;
}

void Advertiser::inc_clicks(){
    Advertiser::total_clicks++;
    BaseAdvertising::inc_clicks();
}

string Advertiser::help(){
    stringstream description;
    description << "get_name(): return name\n"
    << "set_name(): sets new name\n"
    << "inc_clicks(): increment Advertiser and Total clicks by 1\n"
    << "inc_views(): increment Advertiser views by 1\n"
    << "get_clicks(): return number of clicks on all ads\n"
    << "get_views(): return number of views on all ads\n"
    << "get_total_clicks(): total Advertisers clicks\n"
    << "describe_me(): short description of class";
    return description.str();
}

string Advertiser::describe_me(){
    return "Advertiser class keeps track of advertiser information and his ad stats";
}

int Advertiser::get_total_clicks(){
    return total_clicks;
}
