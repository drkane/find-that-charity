# Generated by Django 3.1.1 on 2020-10-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postcode",
            name="pcds",
            field=models.CharField(db_index=True, max_length=8, unique=True),
        ),
    ]
