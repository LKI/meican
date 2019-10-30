from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip
from setuptools import setup

import meican

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="meican",
    version=meican.__version__,
    description="UNOFFICIAL meican command line / sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Lirian Su",
    author_email="liriansu@gmail.com",
    url="https://github.com/LKI/meican",
    license="MIT License",
    entry_points={"console_scripts": ["meican = meican.cmdline:execute"]},
    packages=["meican"],
    install_requires=convert_deps_to_pip(Project(chdir=False).parsed_pipfile["packages"], r=False),
)
