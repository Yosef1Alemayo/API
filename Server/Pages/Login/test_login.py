import requests

class Test_Login:
    URL = 'https://trip-yoetz.herokuapp.com/auth/login'

    def test_login_correctly(self):
        url = Test_Login.URL
        data = {"email": "Yosef@gmail.com",
                "password": "******"}
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert res_data['success'] == True
        assert res_data['message'] == 'login successful'

    def test_login_with_incorrectly_password(self):
        url = Test_Login.URL
        data = {"email": "Yosef@gmail.com",
                "password": "6116161616"}
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
        assert res_data['success'] == False
        assert res_data['message'] == "password or email incorrect"

    def test_login_with_incorrectly_email(self):
        url = Test_Login.URL
        data = {"email": "m@fg", "password": "123456"}
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
        assert res_data['success'] == False
        assert res_data['message'] == "no user found"

    def test_login_with_incorrectly_email_and_password(self):
        url = Test_Login.URL
        data = {"email": "Yo@s", "password": "1526"}
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
        assert res_data['success'] == False
        assert res_data['message'] == "no user found"

