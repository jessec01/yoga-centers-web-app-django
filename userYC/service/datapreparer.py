class DataPreparer:
    def __init__(self, instructor_data: dict, token: str):
        self.instructor_data = instructor_data
        self.token = token
    
    def prepare_instructor_data(instructor_data: dict) -> dict:
        """
        Docstring para prepare_instructor_data
        Prepara los datos del instructor para el registro
        :param instructor_data: Datos del instructor
        :return: Datos preparados del instructor
        """
        prepared_data = {
            "username": instructor_data.get("username"),
            "first_name": instructor_data.get("first_name"),
            "last_name": instructor_data.get("last_name"),
            "email": instructor_data.get("email"),
            "phone": instructor_data.get("phone"),
            "password": instructor_data.get("password"),
        }
        return prepared_data
    def encasulate_data(self) -> dict:
        """
        Docstring para encapsulate_data
        Encapsula los datos en el formato requerido por el servicio de registro
        :param data: Datos del instructor
        :return: Datos encapsulados
        """
        return {
            "instructor": self.instructor_data,
            "token": self.token 
        }