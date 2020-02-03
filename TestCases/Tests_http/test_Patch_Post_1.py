import json
import jsonpath
import requests
import config



def test_patch_update_post_1():
    url = config.base_url_http + config.posts_url + '/' + '1'
    f = open('../jsonFiles/PatchUpdatePost.json', 'r')
    json_request = json.loads(f.read())
    response = requests.patch(url, json_request)
    json_response = response.json()
    user_id = jsonpath.jsonpath(json_response, 'userId')
    id = jsonpath.jsonpath(json_response, 'id')
    title = jsonpath.jsonpath(json_response, 'title')
    body = jsonpath.jsonpath(json_response, 'body')
    assert user_id == ['2']
    assert id == [1]
    assert title == ["Modified title with PATCH"]
    assert body == ["Modified body with PATCH"]
    assert response.status_code == 200

