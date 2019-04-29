# Generated by Django 2.2 on 2019-04-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0005_auto_20190426_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='can_edit',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Возможно редактирование до'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='today',
            field=models.DateField(auto_now_add=True, verbose_name='Сегодня'),
        ),
    ]