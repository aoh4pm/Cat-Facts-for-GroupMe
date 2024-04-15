import pytest
from groupme import GroupMe
from cat_facts import Cats

@pytest.fixture
def access_token():
    return 'YOUR-ACCESS-TOKEN-HERE'


@pytest.fixture()
def group_id():
    return 'YOUR-GROUP-ID-HERE'


def test_cat_facts():
    base = "https://catfact.ninja"
    cat_facts = Cats(base).get_api_response()
    assert cat_facts.status_code == 200


def test_groups_info(access_token):
    group = GroupMe(access_token).get_groups_info()
    assert group.status_code == 200
    assert group.url == f'https://api.groupme.com/v3/groups?{access_token}'


def test_group(access_token, group_id):
    groups = GroupMe(access_token).get_group_single(group_id)
    assert groups.status_code == 200
    assert groups.url == f'https://api.groupme.com/v3/groups/{group_id}?{access_token}'


def test_send_message(access_token, group_id):
    message = "This is a test message"
    group = GroupMe(access_token).send_group_message(group_id, message)
    assert group.status_code == 201



