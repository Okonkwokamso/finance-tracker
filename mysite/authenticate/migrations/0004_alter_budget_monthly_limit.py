# Generated by Django 5.1.7 on 2025-03-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_alter_budget_monthly_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='monthly_limit',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
