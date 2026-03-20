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
