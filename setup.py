from setuptools import setup, find_packages

setup(
    author="@mebaysan",
    author_email="mail@mebaysan.com",
    description="https://tureng.com/en/turkish-english CLI for translation",
    name="tureng-cli",
    version="1.0.0",
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
