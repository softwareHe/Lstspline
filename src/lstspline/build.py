from cffi import FFI
import os
import sysconfig

# Get the directory of this build script
this_dir = os.path.dirname(__file__)

# Initialize CFFI builder
ffibuilder = FFI()

# Define the C API (must match ToyClass_Wrapper.h)
ffibuilder.cdef("""
    typedef void* ToyClassHandle;
    ToyClassHandle ToyClass_create(int size);
    void ToyClass_destroy(ToyClassHandle handle);
    void ToyClass_set_value(ToyClassHandle handle, int index, double value);
    double ToyClass_get_value(ToyClassHandle handle, int index);
    double ToyClass_sum(ToyClassHandle handle);
    int SIZE(ToyClassHandle handle);

    typedef void* StatsClassHandle;
    StatsClassHandle StatsClass_create(ToyClassHandle toyHandle);
    void StatsClass_destroy(StatsClassHandle handle);
    double StatsClass_mean(StatsClassHandle handle);
    double StatsClass_median(StatsClassHandle handle);
    double StatsClass_mode(StatsClassHandle handle);
""")

# Source C++ files
sources = [
    os.path.join(this_dir, "ToyClass.cpp"),
    os.path.join(this_dir, "ToyClass_Wrapper.cpp"),
]

# Extra compiler flags (skip -std=c++11 for MSVC)
cc = (sysconfig.get_config_var('CC') or "").lower()
if 'msvc' in cc:
    extra_compile_args = []
else:
    extra_compile_args = ['-std=c++11']

# Set the CFFI output to be inside the lstspline package
ffibuilder.set_source(
    "lstspline._toyclass",  # <- ensures _toyclass.pyd ends up in lstspline folder
    '#include "ToyClass_Wrapper.h"',
    sources=sources,
    source_extension='.cpp',
    include_dirs=[this_dir],
    extra_compile_args=extra_compile_args,
    language="c++"
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
