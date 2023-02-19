from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in done_with_it/__init__.py
from done_with_it import __version__ as version

setup(
	name="done_with_it",
	version=version,
	description="App for selling old stuffs",
	author="elvis ndegwa",
	author_email="elvisndegwa90@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
