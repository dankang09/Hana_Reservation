# Generated by Django 2.2 on 2022-05-30 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20220530_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics'),
        ),
    ]
