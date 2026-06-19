from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    phone = models.CharField(
        max_length=15,
        verbose_name= 'Телефон',
        blank=True, null=True,
        help_text='Введите номер телефона',
    )

    avatar = models.ImageField(
        upload_to='avatars/',
        default='avatars/default.jpg',
        blank=True,
        null=True,
        verbose_name='Аватар'
    )
    # Страна
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Страна'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
