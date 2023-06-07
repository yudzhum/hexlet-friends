# Generated by Django 4.1.9 on 2023-06-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contributors", "0011_contributionlabel_contribution_labels"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contributionlabel",
            options={
                "verbose_name": "contribution label",
                "verbose_name_plural": "contribution label",
            },
        ),
        migrations.AddConstraint(
            model_name="organization",
            constraint=models.UniqueConstraint(
                fields=("name",), name="unique_organization_name"
            ),
        ),
    ]
