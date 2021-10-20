from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.fields.related import OneToOneField

class Listing(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=100)
    price = models.SmallIntegerField()
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creator_img = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags = models.JSONField(default=dict)

class ListingLikeCount(models.Model):
    listingId = OneToOneField(
        Listing,
        on_delete=models.CASCADE,
        primary_key=True
    )
    like_count = models.IntegerField(default=0)

@receiver(post_save, sender=Listing)
def create_likecount(sender, instance=None, created=False, **kwargs):
    if created:
        ListingLikeCount.objects.create(listingId=instance)