import requests
import config


def test_delete_post_1():
    url = config.base_url_https + config.posts_url + '/' + '1'
    response = requests.delete(url)
    assert response.status_code == 200
