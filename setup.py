from typing import Dict, Final, List

from setuptools import find_packages, setup

from util import write_version_info

package_name: Final[str] = "dicom_phi_check"


requirements: Final[List[str]] = [
    "dicom-anonymizer @ git+https://github.com/medcognetics/dicom-anonymizer.git@v1.0.7-fork",
    "colorama",
    "pydicom @ git+https://github.com/medcognetics/pydicom.git",
]

extras: Final[Dict[str, List[str]]] = {
    "dev": ["pytest", "black", "flake8", "autoflake", "autopep8", "isort", "coverage"]
}

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=package_name,
    version=write_version_info(package_name),
    packages=find_packages(),
    install_requires=requirements,
    extras_require=extras,
    python_requires=">=3.8.0",
    long_description=long_description,
)
