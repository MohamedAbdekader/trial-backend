from django.db import models
from listings.models import Listing
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager

# class CustomAccountManager(BaseUserManager):

#     def create_superuser(self, username, password, **other_fields):

#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_staff=True.')
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True.')

#         return self.create_user(username, password, **other_fields)

#     def create_user(self, username, password, **other_fields):

#         if not username:
#             raise ValueError(_('You must provide an email address'))

#         user = self.model(username=username, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user

class Profile(AbstractUser):
    username = models.CharField(max_length=20, unique=True, db_index=True, primary_key=True)
    watchlist = models.JSONField(default=dict, blank=True, null=True)
    profile_img = models.ImageField(blank=True, null=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def update_profile_img(sender, instance=None, created=False, **kwargs):
#     for listing in Listing.objects.get(creator=instance):
#         if listing.creator_img != Listing.profile_img:
#             listing.creator_img = Listing.profile_img
#             listing.save()
