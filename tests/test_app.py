from http import HTTPStatus


def test_root_deve_retornar_e_ai_mundao(client):
    """
    Esse teste tem 3 etapas (AAA)
    - Arrange: Preparar o ambiente de teste
    - Act: Executar a ação que queremos testar (SUT - System Under Test)
    - Assert: Verificar se o resultado é o esperado
    """

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'E aí, mundão!'}
    assert response.status_code == HTTPStatus.OK


def test_exercicio_ola_mundo_html(client):
    response = client.get('/exercicio-html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olar mundo!!</h1>' in response.text


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
    }


def test_read_users(client):
    response = client.get(
        '/users/',
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'id': 1, 'username': 'alice', 'email': 'alice@example.com'}]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@example.com',
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/50',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found.'}
