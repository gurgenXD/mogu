# Generated by Django 2.2 on 2019-04-24 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0003_auto_20190423_0959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['-posted'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
    ]
