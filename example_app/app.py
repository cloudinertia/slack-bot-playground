import boto3
import time
from chalice import Chalice,Rate
import requests, json

app = Chalice(app_name='demo_app')

SLACK_WEBHOOK="MY_WEBHOOK_URL"

def hello_world():
    now = time.gmtime(time.time())
    return {"text":"hello! current time is :{}".format(now) 

#cronjob
@app.schedule(Rate(1,unit=Rate.DAYS))
def perodic_report(event):
    requests.post(DEVELOPMENT_LOG_WEBHOOK,
                  data=json.dumps(hello_world())
    return "ok"

#webhook( e.g. slash command)
@app.route('/',methods=['POST'],content_types=['application/x-www-form-urlencoded'])
def report(*args):
    return hello_world() 
