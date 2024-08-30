from .models import CustomUser
from .serializers import UserSerializer
from django.core.exceptions import ValidationError


def create_user(data):
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
    else:
        raise ValidationError(serializer.errors)
