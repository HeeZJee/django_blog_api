from posts.models import Post
from rest_framework import generics, permissions
from posts.serializers import PostSerializer
from posts.permissions import IsAuthorOrReadOnly


# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer