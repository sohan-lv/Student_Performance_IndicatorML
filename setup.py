from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    # reading the file
    # -e . is a editable package
    # if -e . is present, we will remove it
    # because it is not a requirement   

    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Sohan",
    author_email="sohanlv1@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)