# Generated by Django 2.2 on 2022-06-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_employee_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', related_name='users', to='login.Employee'),
        ),
    ]
