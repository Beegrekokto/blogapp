"""article_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from article import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('create_article_api/', views.ArticleCreateAPIView.as_view(), name = 'create_article_api'),
    path('update_article_api/', views.ArticleUpdateAPIView.as_view(), name = 'update_article_api'),
    path('view_article_api/', views.ArticleListAPIView.as_view(), name = 'view_article_api'),
    path('detail_article_api/<int:pk>', views.ArticleDetailAPIView.as_view(), name="detail_article_api"),
    path('published_article_api/', views.ArticleListPublishedAPIView.as_view(), name="published_article_api"),
    path('delete_article_api/<int:pk>', views.ArticleDeleteAPIView.as_view(), name="delete_article_api"),
    path('like_api/', views.LikeCreateAPIView.as_view(), name="like_api"),
    path('delete_like_api/', views.LikeDeleteAPIView.as_view(), name="delete_like_api"),
    path('create_comment_api', views.CommentCreateAPIView.as_view(), name="create_comment_api"),
    path('update_comment_api', views.CommentUpdateAPIView.as_view(), name="update_comment_api"),
]
