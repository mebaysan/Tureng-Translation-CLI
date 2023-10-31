from setuptools import setup, find_packages

setup(
    author="@mebaysan",
    description="https://tureng.com/en/turkish-english CLI for translation",
    name="tureng-cli",
    version="1.0.0",
    packages=find_packages(include=["tureng_cli", "tureng_cli.*"]),
    install_requires=["beautifulsoup4", "click", "requests"],
    python_requires=">=3.8",
    entry_points={"console_scripts": ["tureng=tureng_cli.__main__:main"]},
)
