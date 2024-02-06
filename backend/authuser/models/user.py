from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class CustomUserManager(UserManager):
    def _create_user(self, username, password, email, **extra_fields):
        if not email:
            raise ValueError("You have not provided a vaild email address")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(("email address"), unique=True, null=True)
    password = models.CharField(max_length=200)
    phone = models.CharField(blank=False, max_length=50, null=True)

    username = models.CharField(max_length=200, null=True, blank=True, unique=True)
    referralCode = models.CharField(max_length=300, unique=True, editable=False, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    created = models.DateField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "AuthUser"
        verbose_name_plural = "AuthUsers"

    def __str__(self):
        return self.email

    # def get_username(self):
    #     return self.username

    def get_full_name(self):
        return f"{self.email} - {self.username}"

    def get_short_name(self):
        return self.email.split('@')[0]

    def natural_key(self):
        return self.email.split("@")[0]

    def list_display(self):
        return ['pk']

    def list_display_links(self):
        return ['pk']

    def exclude(self):
        return []

    def has_action(self):
        return False

    def is_registered(self):
        return True

CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'