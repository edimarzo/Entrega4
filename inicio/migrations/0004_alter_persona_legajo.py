# Generated by Django 4.1.7 on 2023-04-28 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='legajo',
            field=models.IntegerField(),
        ),
    ]
