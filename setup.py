from setuptools import setup, find_packages

setup(
    name="new-random-topic-generator",
    version="0.2",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "random-topic-generator=random_topic_generator.__main__:main"
        ]
    },
    install_requires=[],
    author="Yuna Suzuki",
    author_email="s2222077@stu.musashino-u.ac.jp",
    description="A simple command line tool to generate random topics.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yuna-musashino/random-topic-generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
