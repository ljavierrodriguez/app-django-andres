# Generated by Django 4.1.3 on 2022-11-04 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('first_name', 'last_name'), 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]
