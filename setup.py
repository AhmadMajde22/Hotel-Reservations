from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "Hotel-Reservations",
    version ="0.1",
    author ="Ahmad Majdi Ba'ra",
    packages = find_packages(),
    install_requires = requirements
)
