# Generated by Django 5.1.6 on 2025-02-16 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_subject'),
        ('account', '0009_remove_studentprofile_section_alter_role_accesses'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Section',
        ),
    ]
