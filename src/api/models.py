from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db import models


class UserManager(DjangoUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        user = self.model(username=username, email=email, **extra_fields)
        user.save()
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        return self.create_user(username, email, password, is_superuser=True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    USERNAME_FIELD = "username"

    username = models.CharField(max_length=255, unique=True, verbose_name="имя пользователя")
    email = models.EmailField()

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
