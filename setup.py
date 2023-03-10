from setuptools import find_packages,setup
from typing import List

Hyphan_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:

    '''
    this function return list of requirements
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','')for req in requirements]

        if Hyphan_e_dot in requirements:
            requirements.remove(Hyphan_e_dot)
    
    return requirements


    


setup(
name = "NEW_MLPROJECT",
version = "0.0.1",
author="Suchita",
author_email="suchikanekar1@gmail.com",
packages=find_packages(),
install_requires =get_requirements('requirements.txt')
)