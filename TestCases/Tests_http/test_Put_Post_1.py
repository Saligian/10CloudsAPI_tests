import json
import jsonpath
import requests
import config



def test_put_update_post_1():
    url = config.base_url_http + config.posts_url + '/' + '100'
    f = open('../jsonFiles/PutUpdatePost.json', 'r')
    json_request = json.loads(f.read())
    response = requests.put(url, json_request)
    json_response = response.json()
    user_id = jsonpath.jsonpath(json_response, 'userId')
    id = jsonpath.jsonpath(json_response, 'id')
    title = jsonpath.jsonpath(json_response, 'title')
    body = jsonpath.jsonpath(json_response, 'body')
    assert user_id == ['2']
    assert id == [100]
    assert title == ["Modified title with PUT"]
    assert body == ["Modified body with PUT"]
    assert response.status_code == 200


