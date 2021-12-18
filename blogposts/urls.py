from django.urls import path

from . import views

urlpatterns = [
    path("", views.GetBlogPosts.as_view()),
    path("<int:pk>/", views.GetBlogPostById.as_view()),
    path("create/", views.AddBlogPost.as_view()),
    path("delete/<int:pk>/", views.DeleteBlogPostById.as_view()),
]
