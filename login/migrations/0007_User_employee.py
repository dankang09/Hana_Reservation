# Generated by Django 2.2 on 2022-06-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_user_following_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='employee',
            field=models.BooleanField(default=False),
        ),
    ]
