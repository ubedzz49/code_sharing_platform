# Generated by Django 5.1.4 on 2024-12-23 19:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_soln'),
    ]

    operations = [
        migrations.AddField(
            model_name='soln',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
