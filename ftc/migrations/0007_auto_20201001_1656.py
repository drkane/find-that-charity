# Generated by Django 3.1.1 on 2020-10-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftc', '0006_auto_20200806_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='postalCode',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Postcode'),
        ),
    ]
