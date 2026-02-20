from setuptools import setup, find_packages

# setup is a method in which we're going to pass several arguments,
# which are the features or attributes or the specifications of our
# package that we're required to include when we make it public.
setup(
    name = 'mypackage',
    version = '0.1',
    packages = find_packages(exclude=['tests*']),
    liscence = 'MIT',
    description = 'EDSA example python package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/PrincewillAnorue/mypackage.git',
    author = 'PrincewillAnorue',
    author_email = 'anorueprincewill@gmail.com'
)