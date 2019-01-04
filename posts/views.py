from rest_framework.generics import ListAPIView

from posts.models import Posts
from posts.serializers import PostSerializer

class PostListAPIView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    

