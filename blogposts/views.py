from rest_framework import generics

from .models import BlogPost
from .serializers import PostSerializer


class AddBlogPost(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer


class GetBlogPosts(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer


class GetBlogPostById(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer


class DeleteBlogPostById(generics.DestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
