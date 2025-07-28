import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Authentication. Use the AZ cli to login into the Azure playground:

    ```bash
    az login --use-device-code
    ```

    And follow the steps to complete the authentication.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Get a handle to the workspace.""")
    return


@app.cell
def _(AuthenticationError):
    import os
    import sys

    from azure.ai.ml import MLClient
    from azure.identity import DefaultAzureCredential
    from dotenv import load_dotenv

    load_dotenv()

    subsciption_id = os.environ.get("SUBSCRIPTION_ID")
    resource_group_name = os.environ.get("RESOURCE_GROUP_NAME")
    workspace_name = os.environ.get("WORKSPACE_NAME")
    compute_cluster = os.environ.get("COMPUTE_CLUSTER")

    required_env_vars = ["SUBSCRIPTION_ID", "RESOURCE_GROUP_NAME", "WORKSPACE_NAME", "COMPUTE_CLUSTER"]

    for var in required_env_vars:
        if not os.environ.get(var):
            print(f"Error: {var} environment variable is missing or empty.")
            sys.exit(1)

    credential = DefaultAzureCredential()

    # Get a handle to the workspace
    try:
        ml_client = MLClient(
            credential=credential,
            subscription_id=subsciption_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name
        )
    except ValueError as e:
        print(f"Invalid input: {str(e)}.")
        sys.exit(1)
    except AuthenticationError as e:
        print(f"Authentication error: {str(e)}.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}.")
        sys.exit(1)

    return ml_client, sys


@app.cell
def _(mo):
    mo.md(r"""Create the custom environment from the Dockerfile and requirements.txt""")
    return


@app.cell
def _(EmptyDirectoryError, ValidationException, ml_client, path, sys):
    from azure.ai.ml.entities import BuildContext, Environment

    env_docker_context = Environment(
        build=BuildContext(
            path="./Docker",
            dockerfile_path="Dockerfile"
        ),
        name="Python312",
        description="Python 3.12 environment."
    
    )
    try:
        ml_client.environments.create_or_update(env_docker_context)
    except ValidationException as e:
        print(f"Validation error: {str(e)}.")
    except EmptyDirectoryError as e:
        print(f"Local path: {path} is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}.")
        sys.exit(1)

    
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
