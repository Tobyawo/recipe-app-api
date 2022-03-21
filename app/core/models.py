from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager (BaseUserManager):


    def  create_user(self, email, password=None, **extra_fields):
        """Create and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user


    def create_superuser(self, email, password):
        """Create and saves a new superuser"""
        user = self.create_user(email, password)  # call the create_user function in existence
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user




# class to override the default user configurations in AbstractBaseUser and PermissionsMixin
class  User(AbstractBaseUser, PermissionsMixin):
        """Custom user model that supports using email instead of username"""
        email = models.EmailField(max_length=255, unique=True)
        name = models.CharField(max_length=255)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)

        objects = UserManager()

        # by default the username field is username but we customise it to email
        USERNAME_FIELD = 'email'