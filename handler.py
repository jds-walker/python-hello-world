import json
import time
 

def hello(event, context):
    print('first second update')
    time.sleep(4)
    print('hello world')
    
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }

