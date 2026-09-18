from app.models.usuario import carregar_usuarios


class AuthController:
    def __init__(self):
        self._usuarios = carregar_usuarios()

    def login(self, nome, senha):
        for usuario in self._usuarios:
            if usuario.mostrar_nome() == nome and usuario.autenticar(senha):
                return {
                    'id': usuario.mostrar_id(),
                    'nome': usuario.mostrar_nome(),
                    'perfil': usuario.perfil(),
                    'permissoes': usuario.permissoes()
                }
        return None