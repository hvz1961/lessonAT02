import responses
import requests
from main2 import get_random_cat_image
@responses.activate
def test_get_random_cat_image_success():
    mock_response = [{'url': 'https://example.com/cat.jpg'}]
    responses.add(responses.GET, 'https://api.thecatapi.com/v1/images/search',
                  json=mock_response, status=200)

    result = get_random_cat_image()
    assert result == 'https://example.com/cat.jpg'
@responses.activate
def test_get_random_cat_image_failure():
    responses.add(responses.GET, 'https://api.thecatapi.com/v1/images/search',
                  status=404)

    result = get_random_cat_image()
    assert result is None