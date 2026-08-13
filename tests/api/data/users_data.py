import pytest


VALID_USER = {
    "name": "Jose Test",
    "username": "jose_test_user",
    "email": "jose_test@example.com",
    "phone": "1-770-736-8031 x56442"
}


UPDATED_USER = {
    "name": "Jose UpdatedTest",
    "username": "jose_updated_test_user",
    "email": "updated_jose@example.com",
    "phone": "1-770-736-8031 x54431"
}


INVALID_USER_IDS = [
    pytest.param(999, id="non-existent-id"),
    pytest.param("abc", id="alphabetic-id"),
    pytest.param(0, id="zero-id"),
    pytest.param(-1, id="negative-id"), 
    pytest.param("$@#", id="special-characters-id")
]


INVALID_USER_PAYLOADS = [
    pytest.param(
        {
            "username": "jose_test_user",
            "email": "jose_test@example.com",
            "phone": "1-770-736-8031 x56442"
        },
        id="missing-name"
    ),
    pytest.param(
        {
            "name": "Jose Test",
            "email": "jose_test@example.com",
            "phone": "1-770-736-8031 x56442"
        },
        id="missing-username"
    ),
    pytest.param(
        {
            "name": "Jose Test",
            "username": "jose_test_user",
            "phone": "1-770-736-8031 x56442"
        },
        id="missing-email"
    ),
    pytest.param(
        {
            "name": None,
            "username": None,
            "email": None,
            "phone": None
        },
        id="null-values"
    ),
    pytest.param(
        {},
        id="empty-payload"
    )
]