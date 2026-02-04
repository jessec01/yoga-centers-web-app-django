from service.register.mainregisterservice import MainRegisterService
class MainService:
    def __init__(self):
        """Initialize MainService.
        defino un statud para el servicio
        """   
        self._register_service = MainRegisterService()
    