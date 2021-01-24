from setuptools import setup

setup(name='freessl',
	version='1.5',
	description='Install Free Let\s Encrypt SSL on RunCloud servers in the easy way.',
	author="Ali Husnain Arshad",
	author_email="info@alihusnain.ml",
	url="https://github.com/alihusnainarshad/freessl",
    download_url = 'https://github.com/alihusnainarshad/freessl/archive/1.5.tar.gz',  
	license="MIT",
	entry_points={
		'console_scripts': [
			'freessl = freessl.freessl:main'
		],
	},
	packages=[
		'freessl'
	],
	install_requires=[
		'python-nginx'
	]
)
