# Generated by Django 5.1.6 on 2025-02-16 10:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0004_delete_section'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('MN', 'Monday'), ('TU', 'Tuesday'), ('WD', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday')], max_length=5)),
                ('period', models.CharField(choices=[('1', '1st Period'), ('2', '2nd Period'), ('3', '3rd Period'), ('4', '4th Period'), ('5', '5th Period'), ('6', '6th Period')], max_length=5)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='academics.grade')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='academics.subject')),
                ('teacher', models.ForeignKey(blank=True, limit_choices_to={'type': 'TE'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('grade', 'day', 'period', 'subject', 'teacher')},
            },
        ),
    ]
