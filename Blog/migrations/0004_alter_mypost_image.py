# Generated by Django 4.1.4 on 2023-04-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_mypost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]