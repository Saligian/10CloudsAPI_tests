import requests
import jsonpath
import config


def test_get_post_13_comments():
    url = config.base_url_https + config.post_id_url + config.post_id_value
    response = requests.get(url)
    json_response = response.json()
    post_id = jsonpath.jsonpath(json_response[0 - 4], 'postId')
    comment_id = jsonpath.jsonpath(json_response[0 - 4], 'id')
    email = jsonpath.jsonpath(json_response[0 - 4], 'email')
    body = jsonpath.jsonpath(json_response[0 - 4], 'body')
    assert post_id is not None
    assert comment_id is not None
    assert email is not None
    assert body is not None
    assert len(json_response) == 5
