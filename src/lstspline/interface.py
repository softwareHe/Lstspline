import numpy as np
from ._toyclass import lib, ffi #imported the library bindings (lib) and ffi interface (ffi)

class ToyClass:
    def __init__(self, size):
        self._obj = lib.ToyClass_create(size) #Create ToyClass object through calling function in C wrapper
        if self._obj == ffi.NULL:
            raise MemoryError("Failed to create ToyClass instance")
        self.size = size # Storing the size of ToyClass array

    def set_value(self, index, value):
        if not (0 <= index < self.size):
            raise IndexError("Index out of range")
        lib.ToyClass_set_value(self._obj, index, float(value)) # Sets single value in the array of toyclass

    def get_value(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Index out of range")
        return lib.ToyClass_get_value(self._obj, index) #gets a single value from the ToyClass array 

    def sum(self):
        return lib.ToyClass_sum(self._obj)# function for sum from c wrapper is returned
    
    
    def set_values(self, values): 
        
        # Used for setting multiple values in the ToyClass array
        
        values = np.asarray(values, dtype=np.float64) # converts input to numpy array
        if values.size != self.size:
            raise ValueError("Input array size does not match")
        for i in range(self.size):
            lib.ToyClass_set_value(self._obj, i, values[i]) #each set value is looped over in C++

    def get_values(self):
        
        # Retrival of all values from Toyclass array to numpy array
        
        arr = np.empty(self.size, dtype=np.float64)
        #For loops to read each value
        for i in range(self.size):
            arr[i] = lib.ToyClass_get_value(self._obj, i)
        return arr
    
    def __del__(self):
        if self._obj != ffi.NULL:
            lib.ToyClass_destroy(self._obj) # destroys the object once garbage is collected  
            self._obj = ffi.NULL


class StatsClass:
    
    def __init__(self, toy_obj: ToyClass):
        self._obj = lib.StatsClass_create(toy_obj._obj)
        if self._obj == ffi.NULL:
            raise MemoryError("Failed to create StatsClass instance")

    def mean(self):
        return lib.StatsClass_mean(self._obj)

    def median(self):
        return lib.StatsClass_median(self._obj)

    def mode(self):
        return lib.StatsClass_mode(self._obj)

    def __del__(self):
        if getattr(self, "_obj", ffi.NULL) != ffi.NULL:
            lib.StatsClass_destroy(self._obj)
            self._obj = ffi.NULL
