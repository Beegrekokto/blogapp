from django.contrib.auth.models import User
from .models import Article, Like, Comment
from rest_framework import  serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('author', 'publication_date', 'headline', 'content', 'published')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('liked_article', 'liked_by', 'like')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('commented_article', 'commented_by', 'comment', 'commented_date')


class UserSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')

