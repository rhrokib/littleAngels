# Generated by Django 3.1.4 on 2020-12-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptionpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='adoption_pics'),
        ),
    ]
