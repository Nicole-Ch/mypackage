from pathlib import Path

from setuptools import find_packages, setup

README = Path(__file__).parent / 'README.md'

setup(
    name='mypackage',
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=README.read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    install_requires=['numpy'],
    url='https://github.com/Nicole-Ch',
    author='Nicole Chao',
    author_email='princesschao2005@gmail.com',
    python_requires='>=3.8',
)