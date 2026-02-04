from instructor.models import Instructor
from magiclink.models import MagicLink
from magiclink.service.tokenmagiclink import TokenLinkService
from magiclink.exception import is_expired_token, is_used_token, is_correct_token, validate_email, validate_tokentype, email_not_found
class ValidateMagicLink:

    _token_service = None

    def __init__(self, token: str):
     
        self._token_service=TokenLinkService(token)
         
    def _validate_tokentype(self):
        
        validate_tokentype(self._token_service.payload)
    def _validate_email(self, email: str, magic_link:MagicLink):
        
        validate_email(email, magic_link)   
    def _validate_jti_token(self, magic_link, jti_token: str):
        
        is_correct_token(magic_link, jti_token)
    def _validate_expired_token(self, magic_link):
        
        is_expired_token(magic_link)
    def _validate_used_token(self, is_used: bool):
        
        is_used_token(is_used)
    def _validate_email_not_found(self, instructor_model: Instructor, email: str):
        email_not_found(instructor_model, email)
    def open_token(self,magic_link, email: str, jti_token: str):
        """
        Docstring para open_token
        Valida el token recibido con las diferentes excepciones definidas en exception.py
        :param self: Descripción
        :param magic_link: Descripción
        :param email: Descripción
        :type email: str
        :param jti_token: Descripción
        :type jti_token: str
        """
        
        self._validate_tokentype()
        self._validate_email(email, magic_link)
        self._validate_jti_token(magic_link, jti_token)
        self._validate_expired_token(magic_link)
        self._validate_used_token(magic_link.is_used)
        self._validate_email_not_found(Instructor, email)
        magic_link.mark()
    