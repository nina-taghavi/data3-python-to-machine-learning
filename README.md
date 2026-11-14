# Python to Machine Learning

Data science coursework, from Python basics to NumPy, Pandas, Matplotlib, scikit-learn and neural networks, with exercises and solutions in Jupyter notebooks.

## Contents

| Folder | Topic | What's inside |
|---|---|---|
| [`01-python-basics`](01-python-basics) | Python basics | Lecture and exercises |
| [`02-numpy`](02-numpy) | Working with arrays (NumPy) | Data types, array basics, ufuncs, aggregates, broadcasting, masks, fancy indexing |
| [`03-pandas`](03-pandas) | Data engineering (Pandas) | Series and DataFrames, indexing, missing values, merge/join, grouping, strings, reading files, review exercises |
| [`04-matplotlib`](04-matplotlib) | Data visualisation (Matplotlib and Seaborn) | Line and scatter plots, histograms, Seaborn, exercises (candy bars, flights, Titanic) |
| [`05a-ml-basics`](05a-ml-basics) | Machine learning basics (scikit-learn) | What ML is, scikit-learn, hyperparameters and validation, pipelines |
| [`05b-ml-techniques`](05b-ml-techniques) | Machine learning techniques (scikit-learn) | Linear regression, decision trees and random forests, k-means, review exercises |
| [`06-neural-networks`](06-neural-networks) | Artificial neural networks (Keras) | Classification and regression |
| [`quick-notes`](quick-notes) | My own summary notes | One notebook per topic |
| [`simple-projects`](simple-projects) | Practice projects | Exam-style projects |

## File naming

All folders and notebooks use **lowercase-with-dashes**:

| Pattern | Meaning |
|---|---|
| `NN.MM-topic.ipynb` | Lecture notebook |
| `NN.MM-topic-exercises.ipynb` | Exercises for that lecture, **with solutions** |
| `review-exercise-topic.ipynb` | Larger review exercise, with solution |
| `exercise-N.M-topic.ipynb` | Numbered exercise, with solution |

Data files are in a `data/` folder next to the notebooks that use them. Images are in `figures/` or `images/`.

## Getting started

First, get the code:

```bash
git clone https://github.com/nina-taghavi/python-to-machine-learning.git
cd python-to-machine-learning
```

Then choose **one** of the two options below.

### Option 1: Virtual environment (venv) with Python 3.13

A virtual environment keeps this project's packages separate from the rest of your computer.

**1. Install Python 3.13** (skip this if `python3.13 --version` already works)

- **macOS:** download it from [python.org](https://www.python.org/downloads/), or run `brew install python@3.13`
- **Windows:** download it from [python.org](https://www.python.org/downloads/) and tick **"Add python.exe to PATH"** during installation
- **Linux (Ubuntu/Debian):** `sudo apt install python3.13 python3.13-venv`

**2. Create the virtual environment** (once, in the repo folder)

```bash
python3.13 -m venv .venv          # Windows: py -3.13 -m venv .venv
```

This creates a `.venv` folder. It's in `.gitignore`, so it's never pushed to GitHub.

**3. Activate it** (each time you open a new terminal)

```bash
source .venv/bin/activate         # Windows: .venv\Scripts\activate
```

Your prompt now starts with `(.venv)`. Check with `python --version`, which should show `Python 3.13.x`.

**4. Install the packages** (once)

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**5. Start Jupyter Lab**

```bash
jupyter lab
```

It opens in your browser. To stop it, press `Ctrl+C` in the terminal. To leave the virtual environment, run `deactivate`.

> **VS Code / PyCharm:** choose `.venv` as the Python interpreter or Jupyter kernel for this project.

### Option 2: Docker

Docker runs Jupyter Lab with Python 3.13 and all packages in a container, so you don't need to install Python yourself.

**1. Install and start [Docker Desktop](https://www.docker.com/products/docker-desktop/).**

**2. Build and start the container** (the first build takes a few minutes)

```bash
docker compose -f docker/docker-compose.yml up -d --build
```

**3. Open Jupyter Lab** at <http://localhost:8888>.

The whole repo is shared with the container, so the notebooks you edit there are saved on your computer.

**Stop it:**

```bash
docker compose -f docker/docker-compose.yml down
```

**Rebuild after changing `requirements.txt`:**

```bash
docker compose -f docker/docker-compose.yml up -d --build
```

> Jupyter in this container has no password, so it's only reachable from your own computer (`127.0.0.1`).

## Large data files

Three data files are too big for GitHub, so they're stored in the [**`datasets`** release](https://github.com/nina-taghavi/python-to-machine-learning/releases/tag/datasets) instead:

| File | Size | Used in |
|---|---|---|
| `UofS_access_log` | 223 MB | `03-pandas/review-exercise-weblog.ipynb` |
| `recipeitems.json` | 135 MB | `03-pandas/03.10-working-with-strings.ipynb` |
| `flights.csv` | 41 MB | `04-matplotlib` flights and Seaborn notebooks |

**You don't need to download them yourself.** The notebooks load them through `get_data()` in [`data_utils.py`](data_utils.py):

```python
import sys; sys.path.append('..')
from data_utils import get_data

flights = pd.read_csv(get_data('data/flights.csv'))
```

The first time a notebook runs, `get_data()` downloads the file into the right `data/` folder. After that, it uses the local copy. `.gitignore` keeps these files out of git.

## Credits

Many lecture notebooks are based on the [*Python Data Science Handbook*](https://jakevdp.github.io/PythonDataScienceHandbook/) by Jake VanderPlas, adapted for the course.
