# Generated by Django 4.2.6 on 2024-02-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='verified_by_superuser',
            field=models.BooleanField(default=False),
        ),
    ]