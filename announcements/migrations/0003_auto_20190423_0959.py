# Generated by Django 2.2 on 2019-04-23 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_auto_20190422_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активное'),
        ),
    ]
