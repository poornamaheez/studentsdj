from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserCredsManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(username=username)
        user.set_password(password)  # Hashes the password
        user.save(using=self._db)
        return user

class UserCreds(AbstractBaseUser):
    username = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=255)  # Store hashed password
    last_login = models.DateTimeField(auto_now=True)  # Fix missing field

    objects = UserCredsManager()
    USERNAME_FIELD = 'username'

    USERNAME_FIELD = 'username'
    class Meta:
        managed = False  # Prevents Django from managing the table schema
        db_table = 'user_creds'  # Matches the existing table name

    def __str__(self):
        return self.username
