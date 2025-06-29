from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get(
        '/',
        status_code=HTTPStatus.OK,
        response_model=Message)
def read_root():
    return {'message': 'Inhain mundo!'}


@app.get(
        '/exercicio-html',
        response_class=HTMLResponse)
def exercicio_aula_02():
    return """
        <html>
            <head>
                <title>Fast Zero - Saudações Planeta</title>
            </head>
            <body>
                <h1>Olar mundo!!</h1>
            </body>
        </html>
"""
