# Generated by Django 2.2 on 2022-05-21 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=20)),
                ('branch_num', models.CharField(max_length=4)),
                ('branch_tel', models.CharField(max_length=11)),
                ('branch_address', models.TextField()),
            ],
        ),
    ]
