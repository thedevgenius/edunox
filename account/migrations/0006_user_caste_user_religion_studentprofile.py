# Generated by Django 5.1.6 on 2025-02-15 01:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_section'),
        ('account', '0005_remove_user_role_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='caste',
            field=models.CharField(choices=[('GN', 'General'), ('SC', 'SC'), ('ST', 'ST'), ('OB', 'OBC')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='religion',
            field=models.CharField(choices=[('H', 'Hindu'), ('M', 'Muslim'), ('S', 'Sikh'), ('O', 'Other')], max_length=5, null=True),
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField(null=True)),
                ('father_name', models.CharField(max_length=200, null=True)),
                ('father_email', models.EmailField(max_length=254, null=True)),
                ('father_phone', models.CharField(max_length=15, null=True)),
                ('mother_name', models.CharField(max_length=200, null=True)),
                ('mother_email', models.EmailField(max_length=254, null=True)),
                ('mother_phone', models.CharField(max_length=15, null=True)),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academics.grade')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academics.section')),
                ('user', models.OneToOneField(editable=False, limit_choices_to={'role': 'ST'}, on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
