from django.db import models
from profiles.models import Profile
from listings.models import Listing
import uuid

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    creator_img = models.CharField(max_length=500, blank=True, null=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)