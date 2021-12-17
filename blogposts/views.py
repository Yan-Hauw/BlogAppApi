from rest_framework import generics

from .models import BlogPost
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
