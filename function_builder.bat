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
echo azure-monitor-opentelemetry >> requirements.txt
echo azure-monitor-events-extension >> requirements.txt

REM Adding .funcignore file
echo .git* >> .funcignore
echo .vscode >> .funcignore
echo __azurite_db*__.json >> .funcignore
echo __blobstorage__ >> .funcignore
echo __queuestorage__ >> .funcignore
echo local.settings.json >> .funcignore
echo test >> .funcignore
echo .venv >> .funcignore

REM Adding Azure Monitor Metric Demo
echo import os>> metric_example.py
echo from azure.monitor.opentelemetry import configure_azure_monitor>> metric_example.py
echo from opentelemetry import metrics>> metric_example.py
echo.>> metric_example.py
echo def metric_example():>> metric_example.py
echo     # Get azure monitor connection>> metric_example.py
echo     configure_azure_monitor(>> metric_example.py
echo         connection_string=os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING") or "",>> metric_example.py
echo     )>> metric_example.py
echo.>> metric_example.py
echo     # Get the meter to record data.>> metric_example.py
echo     meter = metrics.get_meter_provider().get_meter("OpenTelemetry Meter")>> metric_example.py
echo.>> metric_example.py
echo     value = 300>> metric_example.py
echo.>> metric_example.py
echo     # Record employee values to the histogram.>> metric_example.py
echo     histogram = meter.create_histogram("metric_name")>> metric_example.py
echo     histogram.record(value, {"KEY": "VALUE"})>> metric_example.py