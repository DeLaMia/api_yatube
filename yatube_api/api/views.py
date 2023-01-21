from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from posts.models import Comment, Group, Post
from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .permission import IsAdminPermission, IsAuthorPermission
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    permission_classes=(IsAuthenticated, IsAuthorPermission)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    #def perform_create(self, serializer):
    #    if serializer.instance.author != self.request.user:
    #        raise PermissionDenied('Sozdanie контента запрещено!')
    #    super(PostViewSet, self).perform_update(serializer) 
#
    #def perform_update(self, serializer):
    #    if serializer.instance.author != self.request.user:
    #        raise PermissionDenied('Изменение чужого контента запрещено!')
    #    super(PostViewSet, self).perform_update(serializer) 
#
    #def perform_destroy(self, serializer):
    #    if serializer.author != self.request.user:
    #        raise PermissionDenied('Изменение чужого контента запрещено!')
    #    super(PostViewSet, self).perform_destroy(serializer)     

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes=(IsAuthenticated, IsAuthorPermission)

    def get_queryset(self):
        post_id=self.kwargs.get('post_id')   
        post=get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id=self.kwargs.get('post_id')
        instance=get_object_or_404(Post,id=post_id)
        serializer.save(author=self.request.user, post=instance)  
#
    #def perform_destroy(self, serializer):
    #    if serializer.author != self.request.user:
    #        raise PermissionDenied('Изменение чужого контента запрещено!')
    #    super(CommentSerializer, self).perform_destroy(serializer)     
