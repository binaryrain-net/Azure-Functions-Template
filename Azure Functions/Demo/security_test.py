import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.queue_trigger(arg_name="azqueue", queue_name="queuedemo",
                               connection="DefaultEndpointsProtocol=https;AccountName=testdaata;AccountKey=gzDlafdadfguBf9tggQQkBWoa/qS2CjMn9Ig3224OvkDyadf1aXmCbHcCa5Mbi3FsvyadfVoLn+AStkhcKaA==;EndpointSuffix=core.windows.net") 
def queue_trigger(azqueue: func.QueueMessage):
    logging.info('Python Queue trigger processed a message: %s',
                azqueue.get_body().decode('utf-8'))