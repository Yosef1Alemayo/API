import requests
class Register:
    def __init__(self):
        self.url = 'https://trip-yoetz.herokuapp.com/auth/register'

    def test_register_correctly(self):
        data = {
                  "name": "Min",
                  "lastName": "Mun",
                  "email": "f1uasul@gmail.com",
                  "password": "1544444446",
                  "image": "gg",
                  "birthDate": "2003-12-30"
                }
        x = requests.post(self.url, data=data)
        assert x.status_code == 200
        assert x.elapsed.total_seconds() < 15

    def test_register_with_incorrectly_name(self):
        data = {
            "name": "",
            "lastName": "",
            "email": "d1ase@gmail.com",
            "password": "1544444446",
            "image": "gg",
            "birthDate": "2003-12-30"
        }
        x = requests.post(self.url, data=data)
        print(x.status_code)
        assert x.elapsed.total_seconds() < 15
