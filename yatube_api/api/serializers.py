from posts.models import Comment, Group, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author=serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','slug', 'description',)
        model = Group      


class CommentSerializer(serializers.ModelSerializer):
    author=serializers.SlugRelatedField(read_only=True,slug_field='username')
    post=serializers.ReadOnlyField(read_only=True, source='post.pk')
    class Meta:
        fields = ('id','author','post', 'text','created',)
        model = Comment        