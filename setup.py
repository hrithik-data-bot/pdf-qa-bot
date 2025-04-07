"""
Once the project is set-up, run the following command on the console
to make use of the entry-points:
>>> pip install -e .

This will enable user to run the module from the command line
following way:
>>> newyork-taxi-fare-prediction
"""

# type: ignore
# pylint: skip-file

from setuptools import find_packages, setup
import versioneer


requirements = [
    # package requirements (other than Python) go here
    # add required dependencies that are also specified in conda.yaml

]

setup(
    name='newyork-taxi-fare-prediction',
    version=versioneer.get_version(),
    packages=find_packages(where='.', exclude=['tests', 'tests.*']),
    install_requires=requirements,
    keywords='newyork-taxi-fare-prediction',
    classifiers=[
        'Programming Language :: Python :: 3.10.6',
    ],
    entry_points={
        'console_scripts': [
            'newyork-taxi-fare-prediction = newyork_taxi_fare_prediction.cli:main'
        ]
    }
)
