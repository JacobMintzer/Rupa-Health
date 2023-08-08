import requests

mgdata = {
"to": "jrmintz3@gmail.com",
"to_name": "Jacob",
"from": "postmaster@sandboxf0f44c49f4844a0da4ad3db58fc19d01.mailgun.org",
"from_name":"Mailgun Sandbox",
"subject": "Hello Jacob",
"body": "Congratulations Jacob, you just sent an email with Mailgun!  You are truly awesome!"
}

class MailgunClient:
    def __init__(self, secrets):
        self.api_key = secrets["mailgun_api_key"]
        self.endpoint = secrets["mailgun_endpoint"]

    def send_email(self,to, to_name, from_email, from_name, subject, body):
        url = f"https://api.mailgun.net/v3/{self.endpoint}/messages"
        data = {
            "from": f"{from_name} <{from_email}>",
            "to": f"{to_name} <{to}>",
            "subject": subject,
            "text": body,
            }
        auth = ("api",self.api_key)
        try:
            result = requests.post(url=url,auth=auth,data=data)
            return result.ok
        except Exception:
            return False
    
    def get_name(self):
        return "mailgun"