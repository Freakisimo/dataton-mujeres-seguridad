from setuptools import find_packages, setup

setup(
    name="data_integration",
    packages=find_packages(exclude=["data_integration_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "requests",
        "pandas",
        "bs4",
        "boto3",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
