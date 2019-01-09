import os
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

version = os.environ['VERSION'] or '0.1.0'

setuptools.setup(
    name='blink-celery',
    version=version,
    author='Daniel Munoz',
    author_email='dmunozg@gmail.com',
    description='Library to create/execute celery tasks for blink cameras',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=[
        'blink-cameras',
        'celery'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent'])
