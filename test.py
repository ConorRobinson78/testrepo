"""Install required packages, download the dataset, and load it with pandas."""

# Prepare utilities for downloading files and managing installations.

from pathlib import Path
from subprocess import CalledProcessError, run
from urllib.request import urlretrieve
import importlib
import sys

import pandas as pd


def install_packages(packages: list[tuple[str, str]]) -> None:
    """Install each package using pip for the active interpreter."""

    for install_name, _ in packages:
        print(f"Installing {install_name}...")
        try:
            run([sys.executable, "-m", "pip", "install", install_name], check=True)
        except CalledProcessError as exc:
            raise RuntimeError(f"Failed to install {install_name}") from exc


def verify_imports(packages: list[tuple[str, str]]) -> None:
    """Import each package to confirm availability."""

    for _, import_name in packages:
        print(f"Importing {import_name}...")
        importlib.import_module(import_name)


def download_auto_csv(destination: Path) -> Path:
	"""Fetch the dataset and write it to the destination path."""

	url = (
		"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
		"IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/"
		"auto.csv"
	)
	urlretrieve(url, destination)
	return destination


if __name__ == "__main__":
	# Define which packages to grab and how they map to their import names.
	packages_to_install = [
		("pandas", "pandas"),
		("numpy", "numpy"),
		("matplotlib", "matplotlib"),
		("seaborn", "seaborn"),
		("scikit-learn", "sklearn"),
		("statsmodels", "statsmodels"),
	]

	# Ensure everything required is present before continuing.
	install_packages(packages_to_install)
	verify_imports(packages_to_install)

	# Pull the dataset into this folder so later steps can read it.
	target_file = download_auto_csv(Path("auto.csv"))
	print(f"Downloaded dataset to {target_file.resolve()}")

	# Load the CSV into a DataFrame and preview the first rows.
	df = pd.read_csv(target_file)
#EDA
print(df.head())  
print(df.describe)
print(df.info())
print(df.columns)   