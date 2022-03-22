from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, AuthTokenSerializer


# class for managing create user api
# CreateAPIView is pre-made for us to easily make a API that creates
# an object in a database using the serializer that we are going to provide
# All we need is a class variable that points to the serializer class that
# we want to use to create the object
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """ Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    # we can set our renderer class to be able to view this endpoint on browser
    # This means we can login using Chrome etc to make post request instead of only postman, curl etc
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
