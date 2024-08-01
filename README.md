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
- [Azure Functions Core Tool](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python)
- Azure Function App (for further detail on how to set it up, go to [Next Steps (Deployment)](https://github.com/binaryrain-net/Azure-Functions-Template?tab=readme-ov-file#next-steps-deployment)

## Description
The [function_builder](function_builder.bat) file is a batch file designed to automate the setup of a Python-based Azure Function within a virtual environment. To activate it, just put the batch file inside the root directory and execute it. 

Here are the main steps of the process:

- **Creating a Virtual Environment:** The script then creates a Python virtual environment in the current directory. This isolates the Python environment for the Azure Function, preventing any conflicts with other Python projects on the same system.

- **User Input for Function Name:** The script prompts the user to enter a name for the Azure Function.

- **Creating the Azure Function:** The script creates a new directory named "Azure Functions", navigates into it, and then creates a new Azure Function with the provided name. The function is created with the Python worker runtime, using the v2 model, and the "Http Trigger" template for demo purpose..

- **Updating the Requirements File:** The script navigates into the newly created Azure Function's directory and overwrites the requirements.txt file with a new set of dependencies.

## Next Steps (Local)
- Activate the Virtual Environment
    In order to start a virtual environment it is important to install the python module [VENV](https://docs.python.org/3/library/venv.html).

    With the following command you can create a virtual env in the current directory:
    ```bash
    python -m venv .venv
    ```
    
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

## Deployment with Github Actions
In order to use Github Actions for automatic deployment you have to adjust some settings.
First make sure that you save the publish profile from your function:
- In your Repo, go to [SETTINGS > SECRETS AND VARIABLES > ACTIONS] and store the publish profile from your azure function.
- Go to the [workflow](./.github/workflows/azure-functions.yml) and adjust the commented parts (the ones that start with "set this to your.....") to fit your own situation

Now when your code is ready for production, merge your code to the ["azure-production"] branch and the github action will deploy.

> Warning:
> If you enter the github action like the following: `Azure/functions-action@v1` it does not always use the latest release. As explained in the [chapter below](#Consumption-plans), for flex consumption it is important that you at least use the `1.5.2` version: `Azure/functions-action@v1.5.2`

## Consumption plans
If you are working with large files and want the function to handle them, the default consumption with its default RAM is probably not enough. With this in mind, Microsoft created another consumption plan called [Flex consumption](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan). This consumption plan has double the RAM and other features (including virtual network support). The downside though: some usual helpful features and properties are not (or not yet) supported. For further information regarding deprecations please click [here](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#flex-consumption-plan-deprecations).

This repository contains an examplary [workflow](./.github/workflows/azure-functions.yml) that is set up for the flex consumption plan. If you want to use it, make sure that you remove the `.example` at the end of the yml extension and replace the current workflow.


> Keep in mind that when you are using the flex consumption plan, setting up a connectionstring and app settings for the function app contain specific presets (for example: AzureWebJobs….)

