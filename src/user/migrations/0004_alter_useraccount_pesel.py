# Generated by Django 4.2.9 on 2024-02-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_useraccount_pesel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="useraccount",
            name="pesel",
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name="PESEL"),
        ),
    ]
