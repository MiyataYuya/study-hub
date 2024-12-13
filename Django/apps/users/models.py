from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 必要に応じて追加のフィールドを定義
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
