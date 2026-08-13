
def assert_attributes(data, attributes):
    for attr in attributes:
        assert attr in data

def assert_response_contains_payload(response, payload):
    data = response.json()
    assert isinstance(data, dict)
    for key, value in payload.items():
        assert data[key] == value
    return data

def assert_response_is_non_empty_list(response):
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    return data
