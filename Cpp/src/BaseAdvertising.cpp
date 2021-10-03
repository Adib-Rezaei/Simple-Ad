#include <iostream>
#include "BaseAdvertising.hpp"
using namespace std;


int BaseAdvertising::get_clicks(){
    return clicks;
}

int BaseAdvertising::get_views(){
    return views;
}

void BaseAdvertising::inc_clicks(){
    clicks++;
}

void BaseAdvertising::inc_views(){
    views++;
}

string BaseAdvertising::describe_me(){
    return "Base Advertising class is a base class that tracks views and clicks";
}