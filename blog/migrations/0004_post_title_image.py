# Generated by Django 3.0.1 on 2020-01-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_image',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
    ]
