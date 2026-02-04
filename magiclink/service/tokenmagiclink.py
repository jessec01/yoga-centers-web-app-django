# magiclink/service/tokenmagiclink.py
from rest_framework_simplejwt.tokens import AccessToken


from yogacenterwebapp.settings import LIFETIME_ACCESS_TOKEN
class TokenLinkService(AccessToken):
    """
    Docstring para TokenLinkService
    Servicio para la gestion de tokens de tipo tokenlink
    """
    tokentype = 'tokenlink'
    lifetime = LIFETIME_ACCESS_TOKEN 
    def get_token(cls, user):
       token = super().for_user(user)
       token['rol'] = user.rol
       token['tokentype'] = cls.tokentype
       return token
    

class CreateTokenLinkService:
    def __init__(self,user: object):
        self._create_token_link(user)
    
    def _create_token_link(self, user: object) -> str:
        
        token = TokenLinkService.get_token(user)
        return str(token)
    