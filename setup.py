import re
from os import path

from setuptools import setup, find_packages

# read the contents of README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pybullet-planning",
    version='0.0.1',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",

    packages=find_packages(include=['pybullet_tools', 'pybullet_tools.*', 'pybullet_tools.motion_planners']),
    install_requires=[
        "numpy",
        "pybullet",
    ],
)
