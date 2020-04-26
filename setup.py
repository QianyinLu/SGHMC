import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="SGHMC", 
    version="0.1",
    author="Qianyin Lu, Zewen Zhang",
    description="Algorithm of Stochastic Gradient Hamiltonian Monte Carlo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['algorithm'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
