# Generated by Django 5.1.4 on 2025-01-18 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_customize", "0004_alter_optionmodel_attribute"),
    ]

    operations = [
        migrations.AlterField(
            model_name="optionmodel",
            name="option_name",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
