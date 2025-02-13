# Generated by Django 5.1.6 on 2025-02-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='user/'),
        ),
    ]
