# Generated by Django 5.1.1 on 2024-09-30 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbhs', '0004_assignment_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='name',
            field=models.TextField(default='Unnamed Assignment', max_length=100),
        ),
    ]
