import azure.functions as func
import logging

app = func.FunctionApp()


@app.queue_trigger(
    arg_name="azqueue", queue_name="queuedemo", connection="QueueConnectionString"
)  # Queue trigger
def queue_trigger(msg: func.QueueMessage):
    """Azure Function triggered by a queue message."""

    azqueue = msg.get_body().decode("utf-8")

    logging.info(
        "Python Queue trigger processed a message: %s",
        azqueue.get_body().decode("utf-8"),
    )
