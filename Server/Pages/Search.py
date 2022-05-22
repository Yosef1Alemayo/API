import requests


class Search:
    def __init__(self):
        self.url = f"https://trip-yoetz.herokuapp.com/api/cities/"

    def test_search_correctly(self, value):
        data = requests.get(self.url+value)
        try:
            assert data.status_code == 304
        except AssertionError:
            print('Failed')
        assert data.elapsed.total_seconds() < 15

    def test_search_incorrectly(self, value):
        data = requests.get(self.url+value)
        assert data.status_code == 404
        assert data.elapsed.total_seconds() < 15
