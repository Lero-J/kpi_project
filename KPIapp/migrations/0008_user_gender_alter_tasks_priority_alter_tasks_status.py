# Generated by Django 4.2.15 on 2024-08-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KPIapp', '0007_user_phone_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], default='MALE', max_length=100),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='priority',
            field=models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High'), ('CRITICAL', 'Critical')], default='LOW', max_length=100),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('NEW', 'New'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done'), ('CANCELED', 'Canceled'), ('EXPIRED', 'Expired')], default='NEW', max_length=100),
        ),
    ]
