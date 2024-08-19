
from setuptools import setup, find_packages

setup(
    name="localparsera",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch",
        "requests",
        "beautifulsoup4",
    ],
    description="Local version of Parsera library for web scraping using local LLMs.",
    author="Your Name",
    author_email="youremail@example.com",
    url="https://github.com/yourusername/localparsera",
)
