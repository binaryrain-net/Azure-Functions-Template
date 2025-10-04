import base64
import json
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="auth_example")
def auth_example(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    principal_header = req.headers.get("x-ms-client-principal")

    decoded = base64.b64decode(principal_header).decode("utf-8")
    principal = json.loads(decoded)
    claims = principal.get("claims", [])

    oid = next((c["val"] for c in claims if c["typ"].endswith("objectidentifier")), None)
    name = next((c["val"] for c in claims if c["typ"] == "name"), None)

    if name:
        return func.HttpResponse(f"Hello, {name}. Your object ID is {oid}.")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or"
            " in the request body for a personalized response.",
            status_code=200,
        )
