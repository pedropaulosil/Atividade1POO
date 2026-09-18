from app.data.usuarios_mock import USUARIOS


class Usuario:
    def __init__(self, id, nome, senha):
        self._id, self._nome, self._senha = id, nome, senha

    def autenticar(self, senha):
        return self._senha == senha

    def mostrar_id(self):
        return self._id

    def mostrar_nome(self):
        return self._nome

    def perfil(self):
        return 'usuário'

    def permissoes(self):
        return []


class Visitante(Usuario):
    def perfil(self):
        return 'visitante'

    def permissoes(self):
        return ['visualizar produtos']


class Contribuidor(Usuario):
    def perfil(self):
        return 'contribuidor'

    def permissoes(self):
        return ['visualizar produtos', 'cadastrar ofertas']


class Moderador(Contribuidor):
    def perfil(self):
        return 'moderador'

    def permissoes(self):
        return super().permissoes() + ['moderar ofertas']


PERFIS = {
    'visitante': Visitante,
    'contribuidor': Contribuidor,
    'moderador': Moderador
}


def carregar_usuarios():
    return [
        PERFIS[u['perfil']](u['id'], u['nome'], u['senha'])
        for u in USUARIOS
    ]