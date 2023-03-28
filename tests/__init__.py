import pytest


@pytest.fixture
def cleanup():
    print("starting")
    yield "Hello"
    print("ending")
