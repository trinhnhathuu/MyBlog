# Generated by Django 4.1.4 on 2023-04-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_mypost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypost',
            name='audio_file',
            field=models.FileField(null=True, upload_to='media/music'),
        ),
    ]
