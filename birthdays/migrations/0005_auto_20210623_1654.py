# Generated by Django 3.2.4 on 2021-06-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdays', '0004_auto_20210623_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthday',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]