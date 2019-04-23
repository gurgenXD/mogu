# Generated by Django 2.2 on 2019-04-22 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('announcements', '0001_initial'),
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='services.Service', verbose_name='Услуга'),
        ),
    ]