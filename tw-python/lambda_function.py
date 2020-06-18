import json
import time

def lambda_handler(event, context):
    try:
        print("Received event: " + json.dumps(event, indent=2))
        #time.sleep(5)
        print("value1 = " + event['key1'])
        print("value2 = " + event['key2'])
        print("value3 = " + event['key3'])
        
        return event['key3']
        
    except KeyError as e:
        return "Undefined key: " + str(e)

