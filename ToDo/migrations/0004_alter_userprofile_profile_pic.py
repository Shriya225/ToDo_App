# Generated by Django 5.1.2 on 2024-12-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='D:\\Shriya_Coding\\Django_work\\ToDo_Project\\media\\profile_pics\\default.avif', null=True, upload_to='profile_pics/'),
        ),
    ]
