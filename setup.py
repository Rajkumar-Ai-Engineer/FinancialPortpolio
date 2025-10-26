from setuptools import setup, find_packages
from typing import List

def get_requirements(filepath:str)->List[str]:
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        requirements = requirements.remove("-e .") if "-e ." in requirements else requirements
    return requirements  

setup(
    name="financePortfolio",
    version="0.0.1",
    author="Rajkumar",
    author_email= "tech84602@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)      