from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """This function returns a list of requirements"""
    requirement_list:List[str] = []
    return requirement_list




setup(
    name =  "Sensor",
    version = "0.0.1",
    author = "Asif Khan",
    author_email = "aasifkhan02@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()#["pymongo 4.2.0"],
)