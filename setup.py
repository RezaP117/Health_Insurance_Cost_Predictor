from setuptools import find_packages, setup 
from typing import List 

E_FLAG = "-e ."
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj: 
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements] 
        
    if E_FLAG in requirements: 
        requirements.remove(E_FLAG)
    return requirements 

setup (
    name = "Health_Insurance_Predictor", 
    version = "0.0.1",
    author = "Reza Pasha", 
    author_email = "rezaknpasha@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)
