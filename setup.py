from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file:
    readme = readme_file.read()


with open(path.join(here, 'VERSION'), encoding='utf-8') as version_file:
    version = version_file.read()

with open(path.join(here, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]


setup(
    name="py_Pokedex",
    version=version,
    description="This is BotCity Pokedex, a pokedex created using the python framework from BotCity",
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    package_data={
        "py_Pokedex": [
            # When adding files here, remember to update MANIFEST.in as well,
            # or else they will not be included in the distribution on PyPI!
            # 'path/to/data_file',
            'resources',
        ]
    },
    install_requires=requirements,
)
