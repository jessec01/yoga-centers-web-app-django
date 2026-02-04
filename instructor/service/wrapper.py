from instructor.service.main_service import MainService
class WrapperMainService:
    def __init__(self):
        self._main_service: MainService = MainService()
    
    def open(self):
        """
        Docstring para open
        valida sin atajar la excepcion
        :param self: 
        """
        