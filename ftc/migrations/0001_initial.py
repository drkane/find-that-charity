# Generated by Django 3.0.6 on 2020-06-19 10:05

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.indexes
import django.db.models.deletion
from django.db import migrations, models

import ftc.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OrganisationType",
            fields=[
                (
                    "slug",
                    models.SlugField(
                        editable=False,
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="OrgidScheme",
            fields=[
                (
                    "code",
                    models.CharField(
                        db_index=True, max_length=200, primary_key=True, serialize=False
                    ),
                ),
                ("data", django.contrib.postgres.fields.jsonb.JSONField()),
                ("priority", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Scrape",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("spider", models.CharField(max_length=200)),
                (
                    "result",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, null=True
                    ),
                ),
                ("start_time", models.DateTimeField(auto_now_add=True)),
                ("finish_time", models.DateTimeField(auto_now=True, null=True)),
                ("log", models.TextField(blank=True, null=True)),
                ("items", models.IntegerField(default=0)),
                ("errors", models.IntegerField(default=0)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("running", "In progress"),
                            ("success", "Finished successfully"),
                            ("errors", "Finished with errors"),
                            ("failed", "Failed to complete"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Source",
            fields=[
                (
                    "id",
                    models.CharField(
                        db_index=True,
                        max_length=200,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("data", django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="OrganisationLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("org_id_a", ftc.models.OrgidField(db_index=True, max_length=200)),
                ("org_id_b", ftc.models.OrgidField(db_index=True, max_length=200)),
                ("spider", models.CharField(db_index=True, max_length=200)),
                (
                    "scrape",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ftc.Scrape"
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ftc.Source"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Organisation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("org_id", ftc.models.OrgidField(db_index=True, max_length=200)),
                (
                    "orgIDs",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=ftc.models.OrgidField(blank=True, max_length=200),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "linked_orgs",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(blank=True, max_length=100),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "alternateName",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(blank=True, max_length=255),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "charityNumber",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "companyNumber",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "streetAddress",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "addressLocality",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "addressRegion",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "addressCountry",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("postalCode", models.CharField(blank=True, max_length=255, null=True)),
                ("telephone", models.CharField(blank=True, max_length=255, null=True)),
                ("email", models.CharField(blank=True, max_length=255, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("url", models.URLField(blank=True, null=True)),
                (
                    "domain",
                    models.CharField(
                        blank=True, db_index=True, max_length=255, null=True
                    ),
                ),
                ("latestIncome", models.BigIntegerField(blank=True, null=True)),
                ("latestIncomeDate", models.DateField(blank=True, null=True)),
                ("dateRegistered", models.DateField(blank=True, null=True)),
                ("dateRemoved", models.DateField(blank=True, null=True)),
                ("active", models.BooleanField(blank=True, null=True)),
                ("status", models.CharField(blank=True, max_length=200, null=True)),
                ("parent", models.CharField(blank=True, max_length=200, null=True)),
                ("dateModified", models.DateTimeField(auto_now=True)),
                (
                    "organisationType",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(blank=True, max_length=255),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                ("spider", models.CharField(db_index=True, max_length=200)),
                (
                    "location",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, null=True
                    ),
                ),
                (
                    "org_id_scheme",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ftc.OrgidScheme",
                    ),
                ),
                (
                    "organisationTypePrimary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organisations",
                        to="ftc.OrganisationType",
                    ),
                ),
                (
                    "scrape",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ftc.Scrape"
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ftc.Source"
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="organisation",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["orgIDs"], name="ftc_organis_orgIDs_6b135b_gin"
            ),
        ),
        migrations.AddIndex(
            model_name="organisation",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["linked_orgs"], name="ftc_organis_linked__006ef0_gin"
            ),
        ),
        migrations.AddIndex(
            model_name="organisation",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["alternateName"], name="ftc_organis_alterna_37835c_gin"
            ),
        ),
        migrations.AddIndex(
            model_name="organisation",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["organisationType"], name="ftc_organis_organis_8a0172_gin"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="organisation", unique_together={("org_id", "scrape")},
        ),
    ]
