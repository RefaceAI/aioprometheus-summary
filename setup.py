import pathlib
import setuptools
from importlib.machinery import SourceFileLoader

version = SourceFileLoader("version", "aioprometheus_summary/version.py").load_module()


def readfile(filename) -> str:
    return pathlib.Path(filename).read_text("utf-8").strip()


setuptools.setup(
    name="aioprometheus-summary",
    version=version.__version__,
    author="RefaceAI",
    author_email="github-support@reface.ai",
    description="Aioprometheus summary with quantiles over configurable sliding time window",
    long_description=readfile("README.md"),
    license="Apache License 2.0",
    url="https://github.com/RefaceAI/aioprometheus-summary",
    packages=["aioprometheus_summary"],
    install_requires=[
        "aioprometheus>=21.9.0",
        "quantile-estimator>=0.1.0",
    ],
    platforms="Platform Independent",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
)
