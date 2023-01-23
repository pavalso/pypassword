from src.pypassword import __version__
from setuptools import setup


name = 'pypassword'

setup(
    name=name,
    version=__version__,
    packages=[
        name
    ],
    package_dir={
        name:'src/%s' % name
    },
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'pypassword = %s.cli:main' % name,
        ],
    },
)
