# Generated by Django 4.0.4 on 2022-05-28 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['image']},
        ),
    ]
