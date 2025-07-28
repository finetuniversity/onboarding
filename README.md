# onboarding-gpu-compute-cluster

This repository helps you using the GPU compute cluster provided by Research IT. This is in no way a comprehensive tutorial, but more a list of steps to get you started with the GPU compute cluster. 

In here you will find the following information to help you submit your first job to the GPU compute cluster.

The Graphical User Interface (GUI) to the Microsoft Azure Machine Learning you can find [here](https://ml.azure.com).


## prerequisites:
* A bash capable terminal. (Either: Linux, MacOS or Windows Subsystem for Linux.)
* Azure command line software installed. ([Download the Azure CLI here](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).)
* Access to the [Azure Machine Learning Studio](https://ml.azure.com) and the GPU compute cluster provided by Research IT. You most likely have this, since you can access this repository.
* Python >= 3.10 (tested with 3.12)

## Getting started

If you are from the University of Applied Science you will need to change tenants in order to see the correct Azure ML Studio workspace 'ResearchCompute'. University of Amsterdam staff should see the workspace automatically.

In this repository there are a couple of (example) scripts:

1. in the [src](src) directory a sample training script.
2. in the root the [azure_ml_example.py](azure_ml_example.py) script, with this script you can submit a training job to the cluster using [Marimo](https://marimo.io) which is an alternative Notebook environment.
3. also in the root the [create_a_custom_environment.py](create_a_custom_environment.py) script, to create a custom environment using a Dockerfile (which is located in the [Docker](Docker) directory).

## Steps:

1. Clone this repository.
2. Download and install the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) software on you device.
3. Open a internet browser and login into ml.azure.com using your user account.
4. Open a terminal and execute the following command: 

```bash
az account clear; az login --use-device-code
```

Copy and paste the URL into the same internet browser you used in step 2 and provide the code. Select your account and follow the steps. 
You can choose `Self-M-365` to set the default subscription.

5. Create an .env file in the root of the repository:

```bash
cat << EOF >> .env
export SUBSCRIPTION_ID="1ab20903-761f-4de3-877b-8f281de0f62c"
export RESOURCE_GROUP_NAME="ai-for-research"
export WORKSPACE_NAME="ResearchCompute"
export COMPUTE_CLUSTER="news-test"
EOF
```

6. Create a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

7. Install the necessary Python packages: 

```bash
pip install -r requirements.txt
```

8. Run Marimo:

```bash
marimo edit
```

Open the `azure_ml_example.py` notebook to start.




