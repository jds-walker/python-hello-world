import json
 

def hello(event, context):
    print('first second update')
    print('hello world')

    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }

