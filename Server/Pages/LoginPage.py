import requests
class Login:
    def __init__(self):
        self.url = 'https://trip-yoetz.herokuapp.com/auth/login'

    def test_login_with_incorrectly_password(self):
        data = {"email": "Yosef@gmail.com", "password": "6116161616"}
        x = requests.post(self.url, data=data)
        assert x.status_code == 400
        assert x.elapsed.total_seconds() < 15

    def test_login_with_incorrectly_email(self):
        data = {"email": "m@fg", "password": "123456"}
        x = requests.post(self.url, data=data)
        assert x.status_code == 400
        assert x.elapsed.total_seconds() < 15

    def test_login_correctly(self):
        data = {"email": "Yosef@gmail.com", "password": "123456"}
        x = requests.post(self.url, data=data)
        assert x.status_code == 200
        assert x.elapsed.total_seconds() < 15

    def test_login_with_incorrectly_email_and_password(self):
        data = {"email": "Yo@s", "password": "1526"}
        x = requests.post(self.url, data=data)
        assert x.status_code == 400
        assert x.elapsed.total_seconds() < 15


