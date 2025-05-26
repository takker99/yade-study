from setuptools import setup

setup(
    name="yade",
    version="0.0.1",
    packages=["yadeimport"],
    package_data={
        "yadeimport": ["py.typed", "*.pyi"],
    },
)