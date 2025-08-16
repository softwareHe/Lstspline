#include "ToyClass_Wrapper.h"
#include "ToyClass.hpp"

extern "C" {

    //obj: pointer to object memory
    //value: data storage in objects array
    //index: position of value in internal array

    // Create a new ToyClass object and return its pointer/handle
    ToyClassHandle ToyClass_create(int size) {
        return new ToyClass(size);
    }

    // Sets the value at a given index in the ToyClass object
    void ToyClass_set_value(ToyClassHandle obj, int index, double value) {
        ToyClass* instance = static_cast<ToyClass*>(obj);
        if (instance) {
            instance->set_value(index, value);
        }
    }

    // Retrieves the value at a given index from the ToyClass object
    double ToyClass_get_value(ToyClassHandle obj, int index) {
        ToyClass* instance = static_cast<ToyClass*>(obj);
        if (instance) {
            return instance->get_value(index);
        }
        return 0.0; 
    }

    // Returns the sum of all values stored in the ToyClass object
    double ToyClass_sum(ToyClassHandle obj) {
        ToyClass* instance = static_cast<ToyClass*>(obj);
        if (instance) {
            return instance->sum();
        }
        return 0.0; 
    }

    int SIZE(ToyClassHandle obj) {
        ToyClass* instance = static_cast<ToyClass*>(obj);
        if (instance) {
            return instance->size();
        }
        return 0; 
    }

    // Delete the ToyClass object and free its memory
    void ToyClass_destroy(ToyClassHandle obj) {
        delete static_cast<ToyClass*>(obj);
    }

    StatsClassHandle StatsClass_create(ToyClassHandle toyHandle) {
        ToyClass* toyPtr = static_cast<ToyClass*>(toyHandle);
        return new StatsClass(toyPtr);

    }

    void StatsClass_destroy(StatsClassHandle handle) {
        delete static_cast<StatsClass*>(handle);
    }

    double StatsClass_mean(StatsClassHandle handle) {
        return static_cast<StatsClass*>(handle)->mean();
    }

    double StatsClass_median(StatsClassHandle handle) {
        return static_cast<StatsClass*>(handle)->median();
    }

    double StatsClass_mode(StatsClassHandle handle) {
        return static_cast<StatsClass*>(handle)->mode();
    }


}
