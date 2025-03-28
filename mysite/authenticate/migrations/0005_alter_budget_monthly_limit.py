# Generated by Django 5.1.7 on 2025-03-22 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_alter_budget_monthly_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='monthly_limit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
