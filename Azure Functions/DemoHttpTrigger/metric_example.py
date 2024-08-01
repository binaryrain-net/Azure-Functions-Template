import os
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry import metrics

def metric_example():
    # Get azure monitor connection
    configure_azure_monitor(
        connection_string=os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING") or "",
    )

    # Get the meter to record data.
    meter = metrics.get_meter_provider().get_meter("OpenTelemetry Meter")

    value = 300

    # Record employee values to the histogram.
    histogram = meter.create_histogram("<METRIC_NAME>")
    histogram.record(value, {"<KEY>": "<VALUE>"})
