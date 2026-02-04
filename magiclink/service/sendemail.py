from django.core.mail import send_mail
class EmailService:
    """
    Service for sending emails.
    """
    def __init__(self):
        pass
    def _send_email(self):
        """
        Docstring para send_email
        
        :param self: Descripción
        """ 
        send_mail(
    'kamau@gmail.com',
    'This is a test email from Django.',
    'stephenkihuni55@gmail.com',
    ['test-recipient@example.com'],
    fail_silently=False,
)
