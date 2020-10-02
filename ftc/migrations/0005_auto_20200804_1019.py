# Generated by Django 3.1 on 2020-08-04 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ftc", "0004_auto_20200728_1409"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organisation",
            name="location",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="orgidscheme",
            name="data",
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name="scrape",
            name="result",
            field=models.JSONField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="source",
            name="data",
            field=models.JSONField(),
        ),
    ]
