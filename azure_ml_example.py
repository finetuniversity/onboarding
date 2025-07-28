import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""Authenticate to the Azure playground using az cli az account clear; az login --use-device-code""")
    return


@app.cell
def _():
    import os

    from azure.ai.ml import MLClient
    from azure.identity import DefaultAzureCredential
    from dotenv import load_dotenv

    load_dotenv()

    subsciption_id = os.environ.get("SUBSCRIPTION_ID")
    resource_group_name = os.environ.get("RESOURCE_GROUP_NAME")
    workspace_name = os.environ.get("WORKSPACE_NAME")
    compute_cluster = os.environ.get("COMPUTE_CLUSTER")

    credential = DefaultAzureCredential()

    # Get a handle to the workspace
    ml_client = MLClient(
        credential=credential,
        subscription_id=subsciption_id,
        resource_group_name=resource_group_name,
        workspace_name=workspace_name
    )

    clusters = ml_client.compute.list()
    for cluster in clusters:
        print(f"Cluster Name: {cluster.name}")
        print(f"Provisioning State: {cluster.provisioning_state}")   

    return compute_cluster, ml_client


@app.cell
def _(ml_client):
    # List all environments in your workspace
    environments = ml_client.environments.list()
    for environment in environments:
        env_versions = sorted(ml_client.environments.list(name=environment.name), key=lambda x: x.version, reverse=True)
        if env_versions:
            print(f"Environment name: {environment.name}. Latest version: {env_versions[0].version}")
        else:
            print(f"No versions found for environment {environment.name}")

    return


@app.cell
def _(compute_cluster, ml_client):
    import time
    from azure.ai.ml import command
    from azure.ai.ml import Input

    # custom_environment_name = "test-drive:6"
    custom_environment_name = "python311"
    custom_environment_versions = sorted(ml_client.environments.list(name=custom_environment_name), key=lambda x: x.version, reverse=True)
    custom_environment_name_and_version = f"{custom_environment_name}:{custom_environment_versions[0].version}"

    try:
        print(f"Looking for compute cluster {compute_cluster}..")
        ml_client.compute.get(compute_cluster)
        print(f"Compute cluster {compute_cluster} found!")

    except:
        print(f"Uh oh. Compute cluster {compute_cluster} not found!")

    job = command(
        inputs=dict(
            num_epochs=30, learning_rate=0.001, momentum=0.9, output_dir="./outputs"
        ),
        compute=compute_cluster,
        environment=custom_environment_name_and_version,
        code="./src/",  # location of source code
        command="python pytorch_train.py --num_epochs ${{inputs.num_epochs}} --output_dir ${{inputs.output_dir}}",
        # command="python test_drive.py",
        experiment_name="pytorch-birds",
        display_name="pytorch-birds-image"
    )

    job = ml_client.jobs.create_or_update(job)
    # print(job)

    # Poll the job status until it's completed
    while True:
        job_status = ml_client.jobs.get(name=job.name)
        print(f"Job status: {job_status.status}")

        if job_status.status in ["Completed", "Failed"]:
            break

        time.sleep(5)  # wait for 5 seconds before polling again


    # Get the output of the job
    output_file_path = f"./output/{job.name}"
    try:
        ml_client.jobs.download(name=job.name, download_path=output_file_path)
        with open(f"./{output_file_path}/artifacts/user_logs/std_log.txt", "r") as f:
            print(f.read())
    except Exception as e:
        print(f"Error downloading {output_file_path}: {e}")       



    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
