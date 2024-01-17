# Azure-Functions-Template
This repository acts as a template for azure functions.

---
- [Azure-Functions-Template](#azure-functions-template)
  - [Description](#description)
  - [Next Steps](#next-steps)

---


## Description
The [function_builder](function_builder.bat) file is a batch file designed to automate the setup of a Python-based Azure Function within a virtual environment. Here are the main steps of the process:

- **Creating a Virtual Environment:** The script then creates a Python virtual environment in the current directory. This isolates the Python environment for the Azure Function, preventing any conflicts with other Python projects on the same system.

- **User Input for Function Name:** The script prompts the user to enter a name for the Azure Function.

- **Creating the Azure Function:** The script creates a new directory named "Azure Functions", navigates into it, and then creates a new Azure Function with the provided name. The function is created with the Python worker runtime, using the v2 model, and the "Http Trigger" template for demo purpose..

- **Updating the Requirements File:** The script navigates into the newly created Azure Function's directory and overwrites the requirements.txt file with a new set of dependencies.

## Next Steps
- Activate the Virtual Environment
    To activate the virtual env you have to run one of the activation applications inside the terminal. For PowerShell use the following command:
        ```bash
        PS C:\> <venv>\Scripts\Activate.ps1
        ```
- Install the dependencies inside the function directory: `pip install -r ./requirements.txt`
- Start the local azure function: `func host start`
  > If the function does not return an exception you should see the localhost:// paths that are now active.