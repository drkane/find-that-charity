# Generated by Django 3.0.6 on 2020-06-08 10:14

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import ftc.models


class Migration(migrations.Migration):

    dependencies = [
        ('ftc', '0002_auto_20200608_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='org_id_scheme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ftc.OrgidScheme'),
        ),
    ]
