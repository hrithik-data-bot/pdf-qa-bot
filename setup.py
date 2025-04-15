"""
Once the project is set-up, run the following command on the console
to make use of the entry-points:
>>> pip install -e .

This will enable user to run the module from the command line
in the following way:
>>> newyork-taxi-fare-prediction
"""

# type: ignore
# pylint: skip-file

from setuptools import find_packages, setup
import versioneer

requirements = [
    'numpy',
    'pandas',
    'matplotlib',
    'seaborn',
    'transformers',
    'python-dotenv',
    'streamlit',
    'fastapi',
    'timm',
    'torch',
    'torchvision',
    'torchaudio'
]

dev_requirements = [
    'autopep8',
    'pylint',
    'ipykernel'
]

setup(
    name='newyork-taxi-fare-prediction',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(where='.', exclude=['tests', 'tests.*']),
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements
    },
    keywords='newyork-taxi-fare-prediction',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'newyork-taxi-fare-prediction = newyork_taxi_fare_prediction.cli:main'
        ]
    }
)
