from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in a3___taxi/__init__.py
from a3___taxi import __version__ as version

setup(
	name="a3___taxi",
	version=version,
	description="Taxi Booking Service",
	author="Acube Innovations Pvt Ltd",
	author_email="rahidrahivk@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
