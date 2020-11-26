import asyncio
import pytest
from aioresponses import aioresponses
from py3tgbot.main import Py3TgBot


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop


@pytest.fixture
def mock_aioresponse():
    with aioresponses() as m:
        yield m


@pytest.fixture(scope="module")
def client_tgbot():
    client = Py3TgBot(token="12345:TG_BOT_TOKEN")
    yield client