from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin, 
    BaseUserManager
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomAccountManager(BaseUserManager):

    def create_superuser(
        self, email, 
        user_name, first_name, 
        password, **other_information):

        other_information.setdefault('is_staff', True)
        other_information.setdefault('is_superuser', True)
        other_information.setdefault('is_active', True)

        if other_information.get('is_staff') is not True:
            raise ValueError(
                'Super user must be assigment to is_staff=True!'
            )
            
        if other_information.get('is_superuser') is not True:
            raise ValueError(
                'Super user must be assigment to is_superuser=True!'
            )

        return self.create_user(
            email, user_name, 
            first_name, password, 
            **other_information)

    def create_user(
        self, email, 
        user_name, 
        first_name,
        password,
        **other_information):

        if not email:
            raise ValueError(
                _('You must be provide an email address!')
            )
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            user_name=user_name,
            first_name=first_name,
            **other_information
        )

        user.set_password(password)
        user.save()

        return user


class Authors(PermissionsMixin, AbstractBaseUser):
    user_name = models.CharField(
        max_length=80,
        unique=True
    )
    first_name = models.CharField(
        max_length=80,
        blank=True
    )
    avatar = models.ImageField(
        _('Image your profile'),
        upload_to='./media',
        null=True,
        default='images/default.jpg'
    )
    email = models.EmailField(
        _('Email address'),
        unique=True
    )
    about = models.TextField(
        _('About you'),
        max_length=500,
        blank=True
    )
    objects = CustomAccountManager()
    is_staff = models.BooleanField(
        default=True
    )
    is_active = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'User_name: {self.user_name}, Name: {self.first_name}'
    