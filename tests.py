import unittest
from unittest import mock

from mailgun import MailgunClient
from sendgrid import SendgridClient

import requests

good_secrets = {
    "sendgrid_api_key": "good",
    "mailgun_api_key": "good",
    "mailgun_endpoint": "test.mailgun.org"
}
bad_secrets = {
    "sendgrid_api_key": "bad",
    "mailgun_api_key": "bad",
    "mailgun_endpoint": "test.mailgun.org"
}

def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, status_code):
            if status_code == 400:
                self.ok=False
            else:
                self.ok=True
    import pdb
    #pdb.set_trace()
    if "headers" in kwargs and kwargs["headers"]["Authorization"]=="Bearer bad":
        return MockResponse(400)
    elif "auth" in kwargs and kwargs["auth"][1]=="bad":
        return MockResponse(400)
    return MockResponse(200)


class TestMail(unittest.TestCase):
    
    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_sendgrid_good(self,mock_post):
        client = SendgridClient(good_secrets)
        result = client.send_email("a","a","a","a","a","<p>test</p>")
        self.assertTrue(result)
    
    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_sendgrid_bad(self,mock_post):
        client = SendgridClient(bad_secrets)
        result = client.send_email("a","a","a","a","a","<p>test</p>")
        self.assertFalse(result)
        

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_mailgun_good(self,mock_post):
        client = MailgunClient(good_secrets)
        result = client.send_email("a","a","a","a","a","<p>test</p>")
        self.assertTrue(result)
    
    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_mailgun_bad(self,mock_post):
        client = MailgunClient(bad_secrets)
        result = client.send_email("a","a","a","a","a","<p>test</p>")
        self.assertFalse(result)
        pass



if __name__ == '__main__':
    unittest.main()