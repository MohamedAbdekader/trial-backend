from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid
from django.db.models.fields.related import OneToOneField

class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=250)
    price = models.SmallIntegerField()
    image1 = models.ImageField(blank=True, upload_to='media/')
    image2 = models.ImageField(blank=True, upload_to='media/')
    image3 = models.ImageField(blank=True, upload_to='media/')
    image4 = models.ImageField(blank=True, upload_to='media/')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creator_img = models.CharField(blank=True, null=True, max_length=500)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    # tags = models.JSONField(default=dict)

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