# Azure-Functions-Template
This repository acts as a template for azure functions.

---
- [Azure-Functions-Template](#azure-functions-template)
  - [Prerequisites](#prerequisites)
  - [Description](#description)
  - [Next Steps (Local)](#next-steps-local)
  - [Next Steps (Deployment)](#next-steps-deployment)

---

## Prerequisites
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Azure Functions Core TOol](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python)
- Azure Function App (for further detail on how to set it up, go to [[#next-steps-deployment]])

## Description
The [function_builder](function_builder.bat) file is a batch file designed to automate the setup of a Python-based Azure Function within a virtual environment. To activate it, just put the batch file inside the root directory and execute it. 

Here are the main steps of the process:

- **Creating a Virtual Environment:** The script then creates a Python virtual environment in the current directory. This isolates the Python environment for the Azure Function, preventing any conflicts with other Python projects on the same system.

- **User Input for Function Name:** The script prompts the user to enter a name for the Azure Function.

- **Creating the Azure Function:** The script creates a new directory named "Azure Functions", navigates into it, and then creates a new Azure Function with the provided name. The function is created with the Python worker runtime, using the v2 model, and the "Http Trigger" template for demo purpose..

- **Updating the Requirements File:** The script navigates into the newly created Azure Function's directory and overwrites the requirements.txt file with a new set of dependencies.

## Next Steps (Local)
- Activate the Virtual Environment
    To activate the virtual env you have to run one of the activation applications inside the terminal. For PowerShell use the following command:
        ```bash
        PS C:\> <venv>\Scripts\Activate.ps1
        ```
- Install the dependencies inside the function directory: `pip install -r ./requirements.txt`
- Start the local azure function: `func host start`
  > If the function does not return an exception you should see the localhost:// paths that are now active.

## Next Steps (Deployment)
- Make sure that you login with the azure CLI:
  ```bash
  az login
  ```
- Create a resource group (either on portal.azure or with the following command):
  ```bash
  az group create --name <RESOURCEGROUPNAME> --location <LOCATION>
  ```
- Create a storage account (either on portal.azure or with the following command):
  ```bash
  az storage account create --name <STORAGEACCOUNTNAME> --location <LOCATION> --resource-group <RESOURCEGROUPNAME> --sku Standard_LRS
  ```
- Create a functionapp (either on portal.azure or with the following command):
  ```bash
  az functionapp create --resource-group <RESOURCEGROUPNAME> --consumption-plan-location <LOCATION> --runtime <RUNTIME> --functions-version 3 --name <FUNCTIONAPPNAME> --storage-account <STORAGEACCOUNTNAME> --os-type Linux
  ```
- To download remote application settings:
  ```bash
  func azure functionapp fetch-app-settings <FUNCTIONAPPNAME>
  ```
- To deploy your created function, use the following command:
  ```bash
  func azure functionapp publish <FUNCTIONAPPNAME>
  ```
