from setuptools import setup

setup(name="duduinvest", 
    version="0.1",
    description="Dudu investments", 
    packages=['duduinvest'],
    install_requires=[
            "matplotlib",
            "numpy",
            "pandas",
            "scikit-learn",
            "plotly"
        ],
    tests_require=["pytest"],
    python_requires=">=3.11",
    zip_safe=False)