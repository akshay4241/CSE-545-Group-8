# Generated by Django 3.0.2 on 2020-02-04 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_transaction', models.BooleanField()),
                ('create_transaction', models.BooleanField()),
                ('authorize_transaction', models.BooleanField()),
                ('transaction_type', models.CharField(max_length=20)),
                ('issue_check', models.BooleanField()),
                ('fund_transfer', models.BooleanField()),
                ('view_account', models.BooleanField()),
                ('create_account', models.BooleanField()),
                ('modify_account', models.BooleanField()),
                ('close_account', models.BooleanField()),
                ('delete_account', models.BooleanField()),
                ('account_type', models.CharField(max_length=20)),
                ('request_type', models.CharField(max_length=20)),
                ('access_logs', models.BooleanField()),
                ('user_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('business_name', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.IntegerField()),
                ('mobile_number', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('birthdate', models.DateTimeField()),
                ('ssn', models.CharField(max_length=9)),
                ('user_type', models.CharField(max_length=10)),
                ('joining_date', models.DateTimeField()),
                ('password', models.CharField(max_length=200)),
                ('privilege_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Privilege')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_account', models.IntegerField()),
                ('to_account', models.IntegerField()),
                ('transaction_value', models.BigIntegerField()),
                ('transaction_date', models.DateTimeField()),
                ('transaction_type', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User')),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField()),
                ('request_subject', models.TextField()),
                ('request_assigned_to', models.IntegerField()),
                ('request_type', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField()),
                ('appointment_subject', models.TextField()),
                ('appointment_assigned_to', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(max_length=20)),
                ('account_balance', models.BigIntegerField()),
                ('creation_date', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User')),
            ],
        ),
    ]