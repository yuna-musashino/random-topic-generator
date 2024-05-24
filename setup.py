from setuptools import setup, find_packages

setup(
    name="random-topic-generator",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "random-topic-generator=random_topic_generator.__main__:main"
        ]
    },
    install_requires=[],
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple command line tool to generate random topics.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/random-topic-generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
