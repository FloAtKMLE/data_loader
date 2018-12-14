from setuptools import setup, find_packages

setup(
    name='data_loader',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    author='KMLE Munich Flo',
    author_email='florian.ludwig@konicaminolta.eu',
    description='A package for loading of image data  ' +
    'with corresponding labels',
    install_requires=[
    ],
    extras_requires=[
    ]
)
