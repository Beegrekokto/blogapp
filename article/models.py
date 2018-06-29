from django.db import models
from django.contrib.auth.models import  User

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publisher', null=False)
    publication_date = models.DateTimeField(auto_now_add=True, null=False)
    headline = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    published = models.BooleanField(default=False,)

    def __str__(self):
        return self.headline


class Like(models.Model):
    liked_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='liked_article', null=False)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_user', null=False)
    like = models.BooleanField(default=False)


class Comment(models.Model):
    commented_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commented_article',
                                          null=False)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commented_user', null=False)
    comment = models.CharField(max_length=255, null=False)
    commented_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
