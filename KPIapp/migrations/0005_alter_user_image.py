# Generated by Django 4.2.15 on 2024-08-21 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KPIapp', '0004_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='images/default_avatar.jpg', null=True, upload_to='images/'),
        ),
    ]
