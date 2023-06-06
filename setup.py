from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return a list of requirements

    '''
    requirements = []
    with open(file_path) as file_obj:
        # as wk libraries in requirement.txt is written in each new line, we will get /n everytime line is changed while reading from file.hence we will try to change the /n to blank.and
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        #as we have added -e . in the requirements file, we dont want it in the requirements becuase it is just to connect to the setup file. so we will do :
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Surbhi',
    author_email='surbhigusain74@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
