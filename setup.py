from setuptools import setup,find_packages
from typing import List


def get_requirements() ->List[str]:
    """This function returns list of requirement for the project"""
    
    requirements_list : List[str] = []
    return requirements_list


setup(
    name = "stud_track",
    version="0.0.1",
    author="Aditya Ugale",
    author_email="adityaugale4652@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements(),
    
)
