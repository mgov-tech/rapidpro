# Generated by Django 2.2.10 on 2020-09-30 20:31

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0123_contactimport_contactimportbatch"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactimport", name="mappings", field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.AlterField(
            model_name="contactimportbatch",
            name="errors",
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name="contactimportbatch", name="specs", field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
