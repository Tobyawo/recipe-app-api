from django.contrib.auth import get_user_model, authenticate
# ugettext_lazy is useful whenever u are outputting any messagesin python to the screen
# its good idea to pass them through translation system so if you ever do add any
# extra languages to your projects you can easily add the language file and it will
# auto convert all of the text to the correct language
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        # specify fields to be converted to and from json
        fields = ('email', 'password', 'name')
        # extra keywords args to configure a few extra settings in our model serializers
        # we can use this to ensure password is write only
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'), username=email, password=password)
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')
        attrs['user'] = user
        return attrs
