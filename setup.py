from setuptools import setup, find_packages
from typing import List


def _read_requirements(name: str='requirements') -> List[str]:
    with open('requirements.txt', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines() if not line.startswith('#')]


setup(
    name='ecs_task_run',
    version='0.0.1',
    author='Konstantin Matyukhin',
    author_email='konstantin.matyukhin@clarivate.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=_read_requirements(),
)
