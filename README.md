# mlemasterclass-base-deployment

## Setup

For my setup, I use a combination of poetry and conda. 
I use conda to set the Python version of my system, and I use poetry to manage my virtual environments. 

So first, make sure poetry and conda are installed, then create a conda base environment with the right version of Python:

```bash
conda create -n python3.10.11 python=3.10.11
```

Then, instruct poetry to use that version of Python:

```bash
poetry env use $(which python)
```

Finally, install the dependencies from the `pyproject.toml` file:

```bash
poetry install
```

# Train Model

First, we need to fit an actual machine learning model to deploy.

In our case, we are going to use the Iris dataset, with a basic scikit-learn model.

To train the model, run:

```bash
python train_model.py
```

This will create a model artifact `model.joblib` inside the `app` directory.