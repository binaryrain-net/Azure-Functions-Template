@echo off

REM Change the directory to the current directory
cd /d "%~dp0"

REM Create a virtual environment
echo Creating virtual environment...
call python -m venv .venv
echo Virtual environment created successfully.

REM Ask the user to enter a Function Name
set /p functionName=Enter the Function Name: 

REM Create the "Azure Functions" folder and move to the created folder
mkdir "Azure Functions"
cd "Azure Functions\"

REM Create an Azure Function in python
echo Creating Azure Function...
func init %functionName% --worker-runtime python --model V2
func new %functionName% --worker-runtime python --model V2
echo Azure Function created successfully.

REM Change the directory to the Azure Functions folder
cd "%~dp0\Azure Functions\%functionName%"

REM Remove the content of the requirements.txt file and add needed requirements
echo. > requirements.txt
echo azure-functions >> requirements.txt
echo azure-identity >> requirements.txt
echo azure-storage-blob >> requirements.txt
echo pandas >> requirements.txt
echo python-dotenv >> requirements.txt
echo pydantic >> requirements.txt

REM Adding .funcignore file
echo .git* >> .funcignore
echo .vscode >> .funcignore
echo __azurite_db*__.json >> .funcignore
echo __blobstorage__ >> .funcignore
echo __queuestorage__ >> .funcignore
echo local.settings.json >> .funcignore
echo test >> .funcignore
echo .venv >> .funcignore