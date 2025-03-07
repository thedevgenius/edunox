# Generated by Django 5.1.6 on 2025-02-16 23:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0006_alter_schedule_unique_together_alter_schedule_day_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together={('day', 'period'), ('day', 'period', 'teacher')},
        ),
    ]
