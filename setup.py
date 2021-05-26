from setuptools import setup

setup(
    name="trak",
    version="0.0.10",
    packages=["src", "src.trak"],
    package_data={'src': ['data/*.dat']},
    entry_points={
        "console_scripts": [
            "trak = src.__main__:main"
        ]
    },
)
