from django.shortcuts import render
from .models import Article, Like, Comment
from rest_framework import mixins
from .permissions import IsOwnerOrReadOnly
from rest_framework import  permissions

from .serializers  import ArticleSerializer, UserSerializer, LikeSerializer, CommentSerializer
from rest_framework import generics

# Create your views here.

class ArticleListPublishedAPIView(generics.ListAPIView):
    model = Article
    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleSerializer

class ArticleListAPIView(generics.ListAPIView):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailAPIView(generics.RetrieveAPIView):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleCreateAPIView(generics.CreateAPIView):
    model = Article
    queryset = Article.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ArticleSerializer

class ArticleUpdateAPIView(generics.UpdateAPIView):
    model = Article
    queryset = Article.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    serializer_class = ArticleSerializer


class ArticleDeleteAPIView(generics.DestroyAPIView):
    model = Article
    queryset = Article.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    serializer_class = ArticleSerializer


class LikeCreateAPIView(generics.CreateAPIView):
    model = Like
    queryset = Like.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LikeSerializer


class LikeDeleteAPIView(generics.DestroyAPIView):
    model = Like
    queryset = Like.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    serializer_class = LikeSerializer


class CommentListAPIView(generics.ListAPIView):
    model = Comment
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CommentSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    model = Comment
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CommentSerializer


class CommentUpdateAPIView(generics.UpdateAPIView):
    model = Comment
    queryset = Comment.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = CommentSerializer


class CommentDeleteAPIView(generics.DestroyAPIView):
    model = Comment
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAdminUser, IsOwnerOrReadOnly,)
    serializer_class = CommentSerializer