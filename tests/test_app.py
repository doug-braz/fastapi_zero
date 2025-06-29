from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_inhain_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - Arrange: Preparar o ambiente de teste
    - Act: Executar a ação que queremos testar (SUT - System Under Test)
    - Assert: Verificar se o resultado é o esperado
    """

    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Inhain mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_exercicio_ola_mundo_html():
    client = TestClient(app)

    response = client.get('/exercicio-html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olar mundo!!</h1>' in response.text
