import pytest

from libpytools.spam.enviador_de_email import Enviador


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['felipe@parisantunes.com.br', 'f3lipe_antunes@hotmail.com']
)
def test_remetente(destinatario):
    enviador=Enviador()
    destinatarios = ['felipe@parisantunes.com.br', 'f3lipe_antunes@hotmail.com']
    resultado = enviador.Enviar(
        destinatario,
        'felipe.p.antunes@hotmail.com',
        'Assunto',
        'Corpo do Email é a mensagem'
    )
    assert destinatario in resultado

