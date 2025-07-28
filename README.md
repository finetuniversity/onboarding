# Welcome!

Hello! This guide is designed to help you get started with the powerful computing resources provided by Research IT. Think of these resources as a supercomputer you can use for demanding tasks, like training artificial intelligence (AI) models.

This document will walk you through the essential steps to run your first program on this system.

You can access the main web interface for the system, called the **Azure Machine Learning Studio**, here: [ml.azure.com](https://ml.azure.com).

## What You'll Need

Before we start, you'll need a few things set up on your computer. Don't worry, we'll walk you through it.

*   **A "Terminal" or "Command-Line" application:** This is a program that lets you type commands directly to your computer.
    *   **On Linux or macOS:** You can use the built-in "Terminal" app.
    *   **On Windows:** We recommend installing **Windows Subsystem for Linux (WSL)**, which gives you a Linux-style terminal on Windows.
*   **Azure Command-Line Software (Azure CLI):** This is a tool from Microsoft that lets you connect to the university's computing resources from your terminal. You can [download it here](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).
*   **Access to the Azure Machine Learning Studio:** You should already have access to this with your university account. It's how you can see this guide!
*   **Python (version 3.10 or newer):** A popular programming language that we'll use to run our programs.

## Getting Started: A Tour of This Project

This folder contains a few key files to help you:

1.  A sample program located in the `src` directory.
2.  A user-friendly notebook called `azure_ml_example.py`. This is the file you will use to submit your work to the powerful computers. We'll be using a tool called **Marimo**, which makes running Python code interactive and fun.
3.  An advanced script, `create_a_custom_environment.py`, for users who need more control. You can safely ignore this for now.

---

## Step-by-Step Guide

Follow these steps to get everything set up and run your first program.

### Step 1: Download This Project Folder

First, you need a copy of all the files in this project on your own computer. If you have a "Clone" or "Download" button on this page, use that to download the files.

### Step 2: Install the Azure CLI

If you haven't already, please install the [Azure CLI software](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest). This tool is essential for connecting your computer to the university's system.

### Step 3: Log In to the Azure Website

Open your web browser and log in to [ml.azure.com](https://ml.azure.com) with your university account. This ensures your account is active before you proceed.

### Step 4: Connect Your Computer to Your Azure Account

Now, let's link your computer to your Azure account. Open your terminal application and type the following command, then press Enter:

```bash
az login --use-device-code
```

This command will show you a code and a web address (like `microsoft.com/devicelogin`).
1.  Open that web address in the same browser you used for Step 3.
2.  Enter the code from your terminal.
3.  Follow the on-screen instructions to approve the login.

This securely connects your terminal to your university account, so you can give it commands.

### Step 5: Create a Configuration File

You will need to create a special file to store some secret credentials. **These will be sent to you via email.**

1.  In the project folder, create a new file named `.env`.
2.  Open this file in a text editor and paste the content you receive in the email.

### Step 6: Set Up a Virtual Workspace for Python

To avoid conflicts with other Python projects, we'll create a dedicated "virtual environment" for this one.

1.  In your terminal, make sure you are in the project folder you downloaded.
2.  Run the following commands one by one:

    ```bash
    # This creates a virtual environment folder named .venv
    python3 -m venv .venv

    # This "activates" the environment
    source .venv/bin/activate
    ```
    You'll know it worked if you see `(.venv)` appear at the beginning of your terminal prompt.

### Step 7: Install Required Python Packages

Our program depends on a few extra Python tools. Let's install them. In the same terminal (with the virtual environment active), run:

```bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file and automatically installs all the necessary packages.

### Step 8: Start the Interactive Notebook!

You're all set! It's time to launch the interactive notebook. Run this command in your terminal:

```bash
marimo edit
```

This will open a new tab in your web browser with the Marimo interface. From there, open the `azure_ml_example.py` file to get started and run your first program on the university's powerful computers. Good luck!
