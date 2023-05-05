import pytest

from vk_urls_validator import validate_url
from vk_urls_validator.utils import exceptions


@pytest.mark.parametrize(
    ('input_url', 'expected_url'),
    (
            ('vk.com/id1', 'https://vk.com/id1'),
            ('http://vk.com/id1', 'https://vk.com/id1'),
            ('https://vk.com/id1', 'https://vk.com/id1'),
    )
)
def test_https_prefix(input_url: str, expected_url: str):
    assert validate_url(input_url) == expected_url


@pytest.mark.parametrize(
    ('input_url', 'expected_url'),
    (
            ('https://vk.com/id1', 'https://vk.com/id1'),
            ('https://vk.ru/id1', 'https://vk.com/id1'),
            ('https://m.vk.com/id1', 'https://vk.com/id1'),
    )
)
def test_host_replacement(input_url: str, expected_url: str):
    assert validate_url(input_url) == expected_url


@pytest.mark.parametrize(
    ('input_url',),
    (
            ('https://vk.com/hello_',),
            ('https://vk.com/some_long_usernameeeeeeeeeeeeeeeeeee',),
            ('https://vk.com/shrt',),
            ('https://vk.com/incorrect_with_.dot', ),
    )
)
def test_invalid_urls(input_url: str):
    try:
        validate_url(url=input_url)
        assert False
    except (exceptions.VKInvalidHashError,):
        assert True
