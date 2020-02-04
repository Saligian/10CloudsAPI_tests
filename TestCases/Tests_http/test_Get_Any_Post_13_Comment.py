import requests
import random
import jsonpath
import config
import json


# Return all comment ids for the specified post.

def get_comment_ids_for_post(postId):
    url = config.base_url_http + config.post_id_url + str(postId)
    response = requests.get(url)
    json_response = json.loads(response.text)
    ids = []
    for element in json_response:
        ids.append(element['id'])

    return ids


# Tests any post 13 comment at random.

def test_get_any_post_13_comment():
    comment_ids = get_comment_ids_for_post(13)
    url = config.base_url_http + config.post_id_url + '&id=' + str(random.choice(comment_ids))
    response = requests.get(url)
    json_response = response.json()
    post_id = jsonpath.jsonpath(json_response, 'postId')
    id = jsonpath.jsonpath(json_response, 'id')
    email = jsonpath.jsonpath(json_response, 'email')
    body = jsonpath.jsonpath(json_response, 'body')
    assert post_id is not None
    assert id is not None
    assert email is not None
    assert body is not None
