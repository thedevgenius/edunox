# Generated by Django 5.1.6 on 2025-02-18 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_alter_fees_options_alter_fees_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fees',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
