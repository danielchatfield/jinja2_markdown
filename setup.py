try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
	name='jinja2_markdown',
	author='Daniel Chatfield',
	author_email='chatfielddaniel@gmail.com',
	version='0.0.3',
	url='http://github.com/danielchatfield/jinja2_markdown_extension',
	py_modules=['jinja2_markdown'],
	description='A jinja2 extension that adds a '
	            '{% markdown %} tag to templates.',
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
	],
	install_requires=[
		'Markdown>=2.3.1',
		'Jinja2>=2.4'
	]
)