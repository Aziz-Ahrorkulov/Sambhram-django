# Generated by Django 4.2.2 on 2023-08-20 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminprofile',
            options={'verbose_name': 'Админ', 'verbose_name_plural': 'Админы'},
        ),
        migrations.AlterField(
            model_name='adminprofile',
            name='role',
            field=models.PositiveIntegerField(choices=[(1, 'Администратор 1'), (2, 'Администратор 2'), (3, 'Администратор 3')]),
        ),
    ]