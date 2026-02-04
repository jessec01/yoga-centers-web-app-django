from magiclink.service.tokenmagiclink import CreateTokenLinkService 
from instructor.api.serializer import InstructorCreateSerializer
class MainRegisterService:
    def __init__(self):
        
        
       """
       Docstring para __init__
       pasos a seguir para inicializar el servicio
       #1 definir el token 
       :param self: Descripción
       #2 el token y magic link se valida
       #3 se envia el email con el magic link
       #4 se valida el envio de email 
       #5 se retorna el resultado del proceso al objeto principal 
       """ 
       self.serializer_service =InstructorCreateSerializer
       self.data=self.serializer_service.create 
       self.token_service =CreateTokenLinkService() 
        