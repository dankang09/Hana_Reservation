# Generated by Django 2.2 on 2022-06-13 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_like_unique_together'),
        ('login', '0004_auto_20220530_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(to='booking.Branch'),
        ),
    ]