#magiclink/exception.py
import datetime
from magiclink.models import MagicLink
from yogacenterwebapp.settings import LIFETIME_ACCESS_TOKEN
from instructor.models import Instructor
class ExceptionMagicLink(Exception):
    """Base exception for Magic Link errors."""
    def __init__(self, status_code, message):
        super().__init__(message)
        self.status_code = status_code
        self.message = message  
    def get_status(self):
        return {"status_code": self.status_code, "message": self.message}
def validate_tokentype(token:dict):
    """
    Docstring para validate_tokentype
    
    :param token: valida el atributo tokentype del objeto token
    :type token: TokenLinkService
    """
    if token.get('tokentype')!='tokenlink':
        raise ExceptionMagicLink(status_code=401, message="The token type is not valid.")
def validate_email(email: str, magic_link: MagicLink):
    if magic_link.email != email:
        raise ExceptionMagicLink(status_code=400, message="The  email  does not match the one in the magic link.")
def is_used_token(is_used: bool):
    if is_used:
        raise ExceptionMagicLink(status_code=400, message="The magic link has already been used.")
def is_correct_token(magic_link: MagicLink,jti: str):
    if not magic_link.is_token_correct(jti):
        raise ExceptionMagicLink(status_code=400, message="The token of the magic link is not correct.")
    
def is_expired_token(magic_link: MagicLink):
    """
    Docstring para is_expired_token
    
    :param magic_link:valida el tiempo de expiracion del magic link en formato datetime
    :type magic_link: MagicLink
    """
    expiration_time = magic_link.created_at + LIFETIME_ACCESS_TOKEN
    if datetime.datetime.now(datetime.timezone.utc) > expiration_time:
        raise ExceptionMagicLink(status_code=400, message="The magic link has expired.") 
def email_not_found(Instructor:Instructor, email: str):
    if Instructor.objects.filter(email=email).first() is None:
        raise ExceptionMagicLink(status_code=404, message="The email address was not found.")