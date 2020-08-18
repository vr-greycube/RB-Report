# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in rb_report/__init__.py
from rb_report import __version__ as version

setup(
	name='rb_report',
	version=version,
	description='Report Designer using ReportBro for Pdf, Excel reports',
	author='greycube.in',
	author_email='info@greycube.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
