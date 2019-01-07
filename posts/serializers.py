from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )

from .models import Posts

post_detail_url = HyperlinkedIdentityField (
        view_name='posts:post-detail'
    )

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = [
            'title',
            'body',
            'created_at',
        ]

class PostListSerializer(ModelSerializer):
    post_url = post_detail_url
    user = SerializerMethodField()
    user_id = SerializerMethodField()
    class Meta:
        model = Posts
        fields = [
            'post_url',
            'user',
            'id',
            'user_id',
            'title',
            'body',
            'created_at',
        ]
    def get_user(self, obj):
        return str(obj.user.username)
    def get_user_id(seld,obj):
        return obj.user.id

class PostDetailSerializer(ModelSerializer):
    post_url = post_detail_url
    class Meta:
        model = Posts
        fields = [
            'post_url',
            'id',
            'title',
            'body',
            'created_at',
        ]
