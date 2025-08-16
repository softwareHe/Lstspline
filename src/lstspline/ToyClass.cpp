#include "ToyClass.hpp"
#include <stdexcept>

ToyClass::ToyClass(int size) : data(size, 0.0) {
    // Initialize vector with size and zero values
}

// Sets or updates a specific element in data vector
void ToyClass::set_value(int index, double value) {
    if (index < 0 || index >= static_cast<int>(data.size())) {
        throw std::out_of_range("Index out of range");
    }
    data[index] = value;
}

// Reads and returns a value at index 
double ToyClass::get_value(int index) const {
    if (index < 0 || index >= static_cast<int>(data.size())) {
        throw std::out_of_range("Index out of range");
    }
    return data[index];
}

//  Returns the size of the data vector
int ToyClass::size() const {
    return static_cast<int>(data.size());
}

// returns the sum of all values in data vector
double ToyClass::sum() const {
    double s = 0.0;
    for (double v : data) {
        s += v;
    }
    return s;
}

StatsClass::StatsClass(ToyClass* toyObj) : toy(toyObj) {
    if (!toy) {
        throw std::invalid_argument("ToyClass pointer is null");
    }
}

double StatsClass::mean() const {
    int n = toy->size();
    if (n == 0) return 0.0;

    return toy->sum() / n;
}

double StatsClass::median() const {
    int n = toy->size();
    if (n == 0) return 0.0;

    std::vector<double> vals(n);
    for (int i = 0; i < n; ++i) {
        vals[i] = toy->get_value(i);
    }
    std::sort(vals.begin(), vals.end());

    if (n % 2 == 0) {
        return (vals[n/2 - 1] + vals[n/2]) / 2.0;
    } else {
        return vals[n/2];
    }
}

double StatsClass::mode() const {
    int n = toy->size();
    if (n == 0) return 0.0;

    std::map<double, int> freq;
    for (int i = 0; i < n; ++i) {
        freq[toy->get_value(i)]++;
    }

    int max_count = 0;
    double mode_val = 0.0;
    for (auto& pair : freq) {
        if (pair.second > max_count) {
            max_count = pair.second;
            mode_val = pair.first;
        }
    }
    return mode_val;
}