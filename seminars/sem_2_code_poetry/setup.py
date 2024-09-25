from setuptools import setup, find_packages

setup(
    name="test_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "scikit-learn>=0.24.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A test package with intentional errors for linting tools",
    long_description=open("sem_scenary.txt").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/test_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)