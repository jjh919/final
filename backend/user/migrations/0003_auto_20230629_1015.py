# Generated by Django 3.1.1 on 2023-06-29 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20230628_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(blank=True, max_length=40, unique=True),
        ),
    ]