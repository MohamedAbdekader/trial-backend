# Generated by Django 3.2.7 on 2021-09-28 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(db_index=True, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]