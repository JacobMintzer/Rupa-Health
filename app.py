from flask import Flask, request, jsonify
import json
import re
from mailgun import MailgunClient
from sendgrid import SendgridClient

app = Flask(__name__)
with open("./secrets.json") as json_data:
    data = json.load(json_data)

sendgrid_client = SendgridClient(data)
mailgun_client = MailgunClient(data)

preference_order = [sendgrid_client, mailgun_client]
data = {
"to": "kplax3@gmail.com",
"to_name": "Mr. Fake",
"from": "jrmintz3@gmail.com",
"from_name":"Jacob",
"subject": "A message from The Fake Family",
"body": "<h1>Your Bill</h1><p>$10</p>"
}

    

@app.route('/email', methods = ['POST'])
def hello():
    request_data = request.get_json()
    to = request_data["to"]
    to_name = request_data["to_name"]
    from_email = request_data["from"]
    from_name = request_data["from_name"]
    subject = request_data["subject"]
    body = request_data["body"]
    if not to or not to_name or not from_email or not from_name or not subject or not body:
        return 'failure: all fields are required', 400
    email_regex = r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
    if not re.match(email_regex,from_email) or not re.match(email_regex,to):
        return 'failure: invalid email', 400
    clean_body = re.sub(r"<[^>]*>","", body)

    for client in preference_order:
        if client.send_email(to, to_name, from_email,from_name,subject,clean_body):
            return f'sent via {client.get_name()}', 200
        
    return 'failure: unable to send', 400