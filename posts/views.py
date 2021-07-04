from rest_framework import viewsets
from django.contrib.auth import get_user_model
from posts.models import Post
from posts.serializers import PostSerializer, UserSerializer
from posts.permissions import IsAuthorOrReadOnly


# Create your views here.    
class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class UserViewSet(viewsets.ModelViewSet): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    