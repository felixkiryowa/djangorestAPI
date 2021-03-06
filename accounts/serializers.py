from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    ModelSerializer
    )

User = get_user_model()

class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        field = [
            'username',
            'password',
            'email',
        ]

