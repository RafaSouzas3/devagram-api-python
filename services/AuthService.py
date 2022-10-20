from models.UsuarioModel import UsuarioLoginModel
from repositories.UsuarioRepository import buscar_usuario_por_email
from utils.AuthUtil import verificar_senha


async def login_service(usuario: UsuarioLoginModel):
    usuario_encontrado = await buscar_usuario_por_email(usuario.email)

    if not usuario_encontrado:
        return {
            "mensagem": "E-mail ou Senha incorretos.",
            "dados": "",
            "status": 401
        }
    else:
        if verificar_senha(usuario.senha, usuario_encontrado['senha']):
            return {
                "mensagem": "Login realizado com sucesso!",
                "dados": usuario_encontrado,
                "status": 200
            }
        else:
            return {
                "mensagem": "E-mail ou Senha incorretos.",
                "dados": "",
                "status": 401
            }