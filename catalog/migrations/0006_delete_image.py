# Generated by Django 5.0 on 2024-06-15 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_rename_images_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
