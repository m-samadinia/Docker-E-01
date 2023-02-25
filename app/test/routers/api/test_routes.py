import pytest


@pytest.mark.endtoend
def test_helloworld_without_name(client):
    response = client.get('/api/routes/helloworld')
    assert response.status_code == 200
    assert response.content.decode("utf-8") == 'Hello Stranger'


@pytest.mark.endtoend
@pytest.mark.parametrize('name, expected',
                         [('mehdi', 'mehdi')])
def test_helloworld_with_name(client, name: str, expected: str):
    response = client.get('/api/routes/helloworld?name=' + name)
    assert response.status_code == 200
    assert response.content.decode("utf-8") == 'Hello ' + expected


@pytest.mark.endtoend
def test_author(client):
    response = client.get('/api/routes/author')
    assert response.status_code == 200
    assert response.content.decode("utf-8") == 'Mehdi Samadinia'
