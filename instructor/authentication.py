from instructor.models import Instructor
from rest_framework import authentication
from rest_framework import exceptions


class InstructorAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_X_INSTRUCTOR_USERNAME')
        if not username:
            raise exceptions.AuthenticationFailed('No instructor username provided')
        try:
            instructor = Instructor.objects.get(user__username=username)
        except Instructor.DoesNotExist:
            raise exceptions.AuthenticationFailed('Instructor not found')
        return (instructor, None)   