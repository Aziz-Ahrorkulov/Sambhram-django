# Generated by Django 4.2.3 on 2023-08-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_app', '0007_rename_status_jobapplication_approval_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]