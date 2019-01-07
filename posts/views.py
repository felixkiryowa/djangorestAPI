from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
) 
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

from .pagination import(
    PostLimitOffsetPagination,
    PostPageNumberPagination
)

from .permissions import IsOwnerOrReadOnly

from posts.models import Posts
from posts.serializers import (
    PostDetailSerializer, 
    PostListSerializer, 
    PostCreateUpdateSerializer
) 


class PostDetailAPIView(RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostDetailSerializer
    

class PostCreateAPIView(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated] 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PostDeleteAPIView(DestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 

    
class PostListAPIView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        'title','body'
    ]
    # pagination_class = PostLimitOffsetPagination
    pagination_class = PostPageNumberPagination


    def get_queryset(self, *args, **kwargs):
        queryset_list = Posts.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title=query) | 
                Q(body=query)  

            ).distinct()
        return queryset_list
    

    

