from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='glasstoneUNLEASHED',
    version='0.0.1',
    description='Fork of Python library for modelling nuclear weapons effects',
    long_description=readme,
    author='Juan Reyes',
    author_email='juanquiviri@gmail.com',
    url='https://github.com/SharpClaw007/glasstoneUNLEASHED',
    license='MIT',
    packages=['glasstone'],
    install_requires=['numpy', 'scipy', 'affine', 'tkinter', 'matplotlib', 'pandas'])
