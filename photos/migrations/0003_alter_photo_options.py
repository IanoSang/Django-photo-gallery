# Generated by Django 4.0.4 on 2022-05-28 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['id']},
        ),
    ]