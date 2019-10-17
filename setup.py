from setuptools import setup, find_packages

from psw_Generator import __version__


setup(
    name='passgen',
    version=__version__,
    url='https://github.com/0Kit/psw_generator/tree/master/psw_Generator',
    packages=find_packages(),
    python_requires='>3.5',
    install_requires=open('requirements.txt').read().split(),
    entry_points={
        'console_scripts': [
            'passgen = psw_Generator.passgen:main',
        ],
    },
)
