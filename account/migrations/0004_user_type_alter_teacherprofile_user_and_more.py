# Generated by Django 5.1.6 on 2025-02-14 11:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_role_accesses'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('TE', 'Teacher'), ('ST', 'Student')], default='ST', max_length=5),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='user',
            field=models.OneToOneField(limit_choices_to={'role': 1}, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='blood_group',
            field=models.CharField(choices=[('ap', 'A +'), ('an', 'A -'), ('bp', 'B +'), ('bn', 'B -'), ('abp', 'AB +'), ('abn', 'AB -'), ('op', 'O +'), ('on', 'O -')], max_length=5, null=True),
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ManyToManyField(to='account.role'),
        ),
    ]
