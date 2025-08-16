#ifndef TOYCLASS_HPP
#define TOYCLASS_HPP

#include <vector>
#include <map>
#include <algorithm>

class ToyClass {
public:
    ToyClass(int size);
    void set_value(int index, double value);
    double get_value(int index) const;
    double sum() const;
    int size() const;
    
private:
    std::vector<double> data;
};

class StatsClass {
public:
    StatsClass(ToyClass* toyObj);

    double mean() const;
    double median() const;
    double mode() const;

private:
    ToyClass* toy;
};

#endif
