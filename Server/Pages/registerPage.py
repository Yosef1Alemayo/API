import requests
class Register:
    def __init__(self):
        self.url = 'https://trip-yoetz.herokuapp.com/auth/register'

    def user_register_correctly(self):
        data = {'{name: "yo", lastName: "ooo", birthDate: "2000-05-05", email: "rik11i@g.com", password: "123456"}'}
        body = requests.post(self.url, data=data)
        assert body.status_code == 200
        assert body.elapsed.total_seconds() < 10
        assert body.text == '{"success":true,"message":"user added successfully"}'
