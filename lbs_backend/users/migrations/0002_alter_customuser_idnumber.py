# Generated by Django 3.2.12 on 2022-06-25 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='IDNumber',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
