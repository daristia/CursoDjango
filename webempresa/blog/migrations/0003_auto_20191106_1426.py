# Generated by Django 2.1.13 on 2019-11-06 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191106_1425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created'], 'verbose_name': 'entrada', 'verbose_name_plural': 'entradas'},
        ),
    ]
