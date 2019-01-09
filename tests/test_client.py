import pytest

from client.client import PhantomClient
from client.connection import Connection


def test_client_creation_calls_import_api(mocker):
    import_mock = mocker.patch.object(PhantomClient, '_import_api')

    client = PhantomClient('http://127.0.0.1:4002')

    assert isinstance(client.connection, Connection)
    assert import_mock.call_count == 1
