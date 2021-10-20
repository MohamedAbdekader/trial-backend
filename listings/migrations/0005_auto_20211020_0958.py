# Generated by Django 3.2.7 on 2021-10-20 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20211020_0528'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingLikeCount',
            fields=[
                ('listingId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='listings.listing')),
                ('like_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='listing',
            name='like_count',
        ),
    ]