import requests
class Login:
    def __init__(self):
        self.url = 'https://trip-yoetz.herokuapp.com/auth/login'

    def test_login_correctly(self):
        data = {"email": "Yosef@gmail.com", "password": "123456"}
        body = requests.post(self.url, json=data)
        assert body.status_code == 200
        assert body.elapsed.total_seconds() < 10
        try:
            assert body.text == '{"success":true,"message":"login successful","token":' \
                                '"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Il9pZCI6IjYyNmU4YzI3' \
                                'YjY1Zjc5ODIzMzIzY2ZhZSIsIm5hbWUiOiJZb3NlZiIsImxhc3ROYW1lIjoiQWxlbWF5b' \
                                'yIsImJpcnRoRGF0ZSI6IjE5ODgtMTEtMjZUMDA6MDA6MDAuMDAwWiIsImVtYWlsIjoiWW' \
                                '9zZWZAZ21haWwuY29tIiwicGFzc3dvcmQiOiIkMmEkMTAkcTljc2xzSk9nWlBsaGE3L3p2' \
                                'WGFrT1d6TWJ0bDlzZ2MxVHU1S1diaGJseDVJeVBTVS9PMHEiLCJpbWFnZSI6ImsucG5nIiwi' \
                                'aXNBZG1pbiI6ZmFsc2UsImxhc3RWaXNpdCI6IjIwMjItMDUtMDFUMDU6NTg6MjMuMDAwWiIsIm' \
                                'NyZWF0ZWRBdCI6IjIwMjItMDUtMDFUMTM6MzM6MjcuODU4WiIsInVwZGF0ZWRBdCI6IjIwMjIt' \
                                'MDUtMDNUMTI6MTM6MjUuMzI0WiIsIl9fdiI6MH0sImlhdCI6MTY1MzQwODAxNSwiZXhwIjoxNjUzN' \
                                'DE4ODE1fQ.-BfBCJT0Ak8I8UHTeZCPPWvaXzgDPzaADS-e7FrXvks"}'
        except AssertionError:
            print('Token Is Not The Same!')

    def test_login_with_incorrectly_password(self):
        data = {"email": "Yosef@gmail.com", "password": "6116161616"}
        body = requests.post(self.url, json=data)
        assert body.status_code == 400
        assert body.elapsed.total_seconds() < 10
        assert body.text == '{"success":false,"message":"password or email incorrect"}'

    def test_login_with_incorrectly_email(self):
        data = {"email": "m@fg", "password": "123456"}
        body = requests.post(self.url, json=data)
        assert body.status_code == 400
        assert body.elapsed.total_seconds() < 10
        assert body.text == '{"success":false,"message":"no user found"}'

    def test_login_with_incorrectly_email_and_password(self):
        data = {"email": "Yo@s", "password": "1526"}
        body = requests.post(self.url, json=data)
        assert body.status_code == 400
        assert body.elapsed.total_seconds() < 10
        assert body.text == '{"success":false,"message":"no user found"}'


