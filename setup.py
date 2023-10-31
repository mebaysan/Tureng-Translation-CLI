import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    author="@mebaysan",
    author_email="mail@mebaysan.com",
    description="https://tureng.com/en/turkish-english CLI for translation",
    name="tureng-cli",
    URL="https://github.com/mebaysan/Tureng-Translation-CLI",
    version="1.0.0",
    long_descp_content="text/markdown",
    long_descp=README,
    packages=find_packages(include=["tureng_cli", "tureng_cli.*"]),
    install_requires=["beautifulsoup4", "click", "requests"],
    python_requires=">=3.8",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    keywords="mebaysan translation Turkish English Tureng CLI",
    zip_safe=False,
    license="MIT",
    entry_points={"console_scripts": ["tureng-cli=tureng_cli.__main__:main"]},
)
