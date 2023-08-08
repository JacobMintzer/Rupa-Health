import requests

class SendgridClient:
    def __init__(self, secrets):
        self.api_key = secrets["sendgrid_api_key"]
        self.url = "https://api.sendgrid.com/v3/mail/send"

    def send_email(self, to, to_name, from_email, from_name, subject, body):
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        data = {
            "personalizations":[{
                "to":[{"email":to,"name":to_name}],

            }],
            "from":{"email":from_email,"name":from_name},
            "subject": subject,
            "content": [{"type":"text/plain","value":body}]
        }
        try:
            result = requests.post(url=self.url,headers=headers,json=data)

            return result.ok
        except Exception:
            return False
        
    def get_name(self):
        return "sendgrid"