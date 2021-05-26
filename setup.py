from setuptools import setup

setup(
    name="trak",
    version="0.0.9",
    packages=["src", "src.trak"],
    entry_points={
        "console_scripts": [
            "trak = src.__main__:main"
        ]
    },
)
