from setuptools import setup

setup(
    name="beebasm-fmt",
    version="0.1.0",
    py_modules=["beebasm_fmt"],
    entry_points={
        "console_scripts": [
            "beebasm-fmt=beebasm_fmt:main",
        ],
    },
    python_requires=">=3.6",
)
