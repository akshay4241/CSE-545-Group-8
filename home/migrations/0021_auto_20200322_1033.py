# Generated by Django 3.0.2 on 2020-03-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20200322_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(default=8093389047, max_length=10, unique=True),
        ),
    ]