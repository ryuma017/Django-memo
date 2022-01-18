from django.db import models
from django.contrib.auth import get_user_model


class Memo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
