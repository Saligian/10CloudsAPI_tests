import requests
import config


# According to the tested API documentation the deletion is only faked to return correct response.
# The data still remains on the server. This case covers the deletion of a single post to check the response.

def test_delete_post_1():
    url = config.base_url_https + config.posts_url + '/' + '1'
    response = requests.delete(url)
    assert response.status_code == 200
