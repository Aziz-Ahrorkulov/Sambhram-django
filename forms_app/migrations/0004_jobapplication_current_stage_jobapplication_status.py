# Generated by Django 4.2.3 on 2023-08-21 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_app', '0003_alter_jobapplication_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='current_stage',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]
