# Generated by Django 5.0.6 on 2024-07-01 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_rename_categoria_acessorio"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="acessorio",
            options={"verbose_name": "Acessorio", "verbose_name_plural": "Acessórios"},
        ),
    ]
