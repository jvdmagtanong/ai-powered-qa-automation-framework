import pytest


VALID_POST = {
    "userId": 1,
    "title": "Jose - Test Post",
    "body": "Testing api - create a post."
}


UPDATED_POST = {
    "id": 1,
    "title": "Updated test post",
    "body": "This post has been updated",
    "userId": 1
}


INVALID_POST_PAYLOADS = [
    pytest.param(
        {"userId": 1, "body": "Test create post."},
        id="missing-title"
    ),
    pytest.param(
        {"userId": 1, "title": "Test Post"},
        id="missing-body"
    ),
    pytest.param(
        {"title": "Test Post", "body": "Test create post"},
        id="missing-user-id"
    ),
    pytest.param(
        {"userId": 999, "title": "Test Post", "body": "Test create post."},
        id="invalid-user-id"
    ),
    pytest.param(
        {"userId": 1, "title": "", "body": ""},
        id="empty-values"
    ),
    pytest.param(
        {},
        id="empty-payload"
    )
]


INVALID_POST_IDS = [
    pytest.param(999, id="non-existent-id"),
    pytest.param(0, id="zero-id"),
    pytest.param(-1, id="negative-id"),
    pytest.param("abc", id="alphabetic-id")
]


def get_invalid_update_post_payload(post_id):
    return {
        "id": post_id,
        **VALID_POST
    }

