"""Download large data files from the GitHub Release the first time they are needed."""
import os
import urllib.request

RELEASE_URL = "https://github.com/nina-taghavi/python-to-machine-learning/releases/download/datasets/"


def get_data(path):
    """Return `path`, downloading the file from the release first if it is missing."""
    if not os.path.exists(path):
        folder = os.path.dirname(path)
        if folder:
            os.makedirs(folder, exist_ok=True)
        name = os.path.basename(path)
        print(f"Downloading {name} ...")
        urllib.request.urlretrieve(RELEASE_URL + name, path)
        print("Done.")
    return path
