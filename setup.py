"""Setup script for python3-telegram-bot-aiohttp"""
import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

requirements = ["aiohttp>=3.6.2"]

setuptools.setup(
	name="py3tgbot",
	version="0.0.1",
	author="Dmitriy Kalekin",
	author_email="herrhorror@gmail.com",
	description="Simple async python 3 telegram bot using fast aiohttp requests",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/DmitriyKalekin/py3tgbot",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3.8",
		"License :: OSI Approved :: MIT",
		"Operating System :: OS Independent",
	],
	install_requires=[
		"aiohttp", "aioresponses",
	],
	python_requires='>=3.7',
)