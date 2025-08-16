from setuptools import setup


setup(
    name="lstspline",
    version="0.1.0",
    packages=["lstspline"],
    package_dir={"": "src"},
    install_requires=["cffi", "numpy"],
    setup_requires=["cffi"],
    cffi_modules=["src/lstspline/build.py:ffibuilder"],
)
