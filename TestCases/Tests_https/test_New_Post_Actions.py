import json
import jsonpath
import requests
import config


def test_add_new_post():
    url = config.base_url_https + config.posts_url
    f = open('../jsonFiles/NewPost.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(url, json_request)
    json_response = response.json()
    user_id = jsonpath.jsonpath(json_response, 'userId')
    id = jsonpath.jsonpath(json_response, 'id')
    title = jsonpath.jsonpath(json_response, 'title')
    body = jsonpath.jsonpath(json_response, 'body')
    assert user_id == ['1']
    assert id == [101]
    assert title == ["New post title"]
    assert body == ["New post body"]
    assert response.status_code == 201


def test_get_new_post():
    url = config.base_url_https + config.posts_url + '/' + config.new_post_id
    response = requests.get(url)
    json_response = response.json()
    user_id = jsonpath.jsonpath(json_response, 'userId')
    id = jsonpath.jsonpath(json_response, 'id')
    title = jsonpath.jsonpath(json_response, 'title')
    body = jsonpath.jsonpath(json_response, 'body')
    assert user_id == ['1']
    assert id == [101]
    assert title == ["New post title"]
    assert body == ["New post body"]
    assert response.status_code == 200


def test_put_update_new_post():
    url = config.base_url_https + config.posts_url + '/' + config.new_post_id
    f = open('../jsonFiles/PutUpdatePost.json', 'r')
    json_request = json.loads(f.read())
    response = requests.put(url, json_request)
    json_response = response.json()
    user_id = jsonpath.jsonpath(json_response, 'userId')
    id = jsonpath.jsonpath(json_response, 'id')
    title = jsonpath.jsonpath(json_response, 'title')
    body = jsonpath.jsonpath(json_response, 'body')
    assert user_id == ['2']
    assert id == [101]
    assert title == ["Modified title with PUT"]
    assert body == ["Modified body with PUT"]
    assert response.status_code == 201


def test_get_put_updated_post():
    url = config.base_url_https + config.posts_url + '/' + config.new_post_id
    response = requests.get(url)
    json_response = response.json()
    user_id = jsonpath.jsonpath(json_response, 'userId')
    id = jsonpath.jsonpath(json_response, 'id')
    title = jsonpath.jsonpath(json_response, 'title')
    body = jsonpath.jsonpath(json_response, 'body')
    assert user_id == ['2']
    assert id == [101]
    assert title == ["Modified title with PUT"]
    assert body == ["Modified body with PUT"]
    assert response.status_code == 200


def test_patch_update_new_post():
    url = config.base_url_https + config.posts_url + '/' + config.new_post_id
    f = open('../jsonFiles/PatchUpdatePost.json', 'r')
    json_request = json.loads(f.read())
    response = requests.patch(url, json_request)
    json_response = response.json()
    user_id = jsonpath.jsonpath(json_response, 'userId')
    id = jsonpath.jsonpath(json_response, 'id')
    title = jsonpath.jsonpath(json_response, 'title')
    body = jsonpath.jsonpath(json_response, 'body')
    assert user_id == ['2']
    assert id == [101]
    assert title == ["Modified title with PATCH"]
    assert body == ["Modified body with PATCH"]
    assert response.status_code == 201


def test_get_patch_updated_post():
    url = config.base_url_https + config.posts_url + '/' + config.new_post_id
    response = requests.get(url)
    json_response = response.json()
    user_id = jsonpath.jsonpath(json_response, 'userId')
    id = jsonpath.jsonpath(json_response, 'id')
    title = jsonpath.jsonpath(json_response, 'title')
    body = jsonpath.jsonpath(json_response, 'body')
    assert user_id == ['2']
    assert id == [101]
    assert title == ["Modified title with PATCH"]
    assert body == ["Modified body with PATCH"]
    assert response.status_code == 200


def test_delete_new_post():
    url = config.base_url_https + config.posts_url + '/' + config.new_post_id
    response = requests.delete(url)
    assert response.status_code == 200


def test_get_deleted_post():
    url = config.base_url_https + config.posts_url + '/' + config.new_post_id
    response = requests.get(url)
    assert response.status_code == 404
