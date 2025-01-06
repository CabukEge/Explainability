from setuptools import setup, find_packages

setup(
    name="explainability",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'torch',
        'scikit-learn',
        'matplotlib'
    ]
)