# Generated by Django 2.2 on 2019-05-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20190514_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='starcolor',
            name='color',
            field=models.CharField(default='#fffffff', max_length=250, verbose_name='Код цвета'),
        ),
    ]