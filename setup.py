from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='contrast_correction',
    version='1.0.0',
    description='Contrast Correction',
    url='https://github.com/DDMAL/contrast_correction',
    author='Khoi Nguyen, Wanyi Lin, Paco Castellanos',
    license='MIT License',
    packages=['contrast_correction'],
    install_requires=requirements,
    python_requires=">=3.7.5"
)