from setuptools import setup

setup(name='asus_stat',
	version='0.1.0',
	description='Utility for getting statistics from ASUS modems.',
	url='https://github.com/cmbrad/asus_stat',
	author='Christopher Bradley',
	author_email='chris.bradley@cy.id.au',
	license='MIT',
	packages=['asus_stat', 'asus_stat.devices', 'asus_stat.providers'],
	zip_safe=False)
