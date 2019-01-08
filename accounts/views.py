from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)
from rest_framework.generics import (
    CreateAPIView
) 

from accounts.serializers import (
    UserCreateSerializer
) 

User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    serializer_class = User
    queryset = User.objects.all()
    
    


    

