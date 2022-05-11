class Enviador:
    def Enviar(self, remetente, destinatario, assunto, mensagem):
        if "@" not in remetente:
            raise EmailInvalido(f'O Email do remetente é invalido: {remetente}')
        return remetente


class EmailInvalido(Exception):
    pass