import pytest

from libpytools.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['felipe@parisantunes.com.br', 'f3lipe_antunes@hotmail.com']
)
def test_remetente(remetente):
    enviador=Enviador()
    resultado = enviador.Enviar(
        remetente,
        'felipe.p.antunes@hotmail.com',
        'Assunto',
        'Corpo do Email é a mensagem'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'f3lipe_antunes']
)
def test_remetente_invalido(remetente):
    enviador=Enviador()
    with pytest.raises(EmailInvalido):
        enviador.Enviar(
            remetente,
            'felipe.p.antunes@hotmail.com',
            'Assunto',
            'Corpo do Email é a mensagem'
            )
