# Generated by Django 5.2 on 2025-04-29 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compagnie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='compagnie/'),
        ),
    ]
