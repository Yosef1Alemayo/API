import requests
class Search:
    def __init__(self):
        self.url = f"https://trip-yoetz.herokuapp.com/api/cities/"

    def test_search_correctly(self, value):
        data = requests.get(self.url+value)
        assert data.status_code == 200
        assert data.elapsed.total_seconds() < 10
        assert data.text == '{"success":true,"data":{"_id":"62278f47583fc9714e39531a",' \
                            '"name":"Jerusalem","description":"Jerusalem is a city located in ' \
                            'modern-day Israel and is considered by many to be one of the holiest ' \
                            'places in the world. Jerusalem is a site of major significance for the ' \
                            'three largest monotheistic religions: Judaism, Islam and Christianity, ' \
                            'and both Israel and Palestine have claimed Jerusalem as a capital city.' \
                            ' Because of these strong, age-old associations, bloody conflicts to control ' \
                            'the city and sites within it have been waged for thousands of years.",' \
                            '"images":["https://cdn.pixabay.com/photo/2018/04/03/16/06/tourism-3287159_1280.jpg"' \
                            ',"https://cdn.pixabay.com/photo/2018/08/27/18/11/kubbetus-sahara-3635632_1280.jpg",' \
                            '"https://cdn.pixabay.com/photo/2015/05/03/20/06/israel-751653_1280.jpg"]}}'

    def test_search_incorrectly_when_city_not_exist(self, value):
        data = requests.get(self.url+value)
        assert data.status_code == 404
        assert data.elapsed.total_seconds() < 10
        assert data.text == '{"success":false,"message":"no city found"}'

    def test_search_incorrectly_with_invalid_value(self, value):
        data = requests.get(self.url + value)
        assert data.status_code == 404
        assert data.elapsed.total_seconds() < 10
        assert data.text == '{"success":false,"message":"no city found"}'