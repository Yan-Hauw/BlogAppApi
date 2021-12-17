from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author_name",
            "title",
            "content",
            "created_at",
        )
        model = models.BlogPost
