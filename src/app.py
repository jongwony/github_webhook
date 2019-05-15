import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def pull_request():
    data = json.loads(request.data)
    if data['action'] == 'closed' and data['pull_request']['merged']:
        return 'OK'
    return 'Exit'
