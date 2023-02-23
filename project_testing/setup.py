from setuptools import find_packages, setup

setup(
    name="project_testing",
    packages=find_packages(exclude=["project_testing_tests"]),
    install_requires=[
        "dagster",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
