# Generated by Django 4.0.6 on 2022-07-12 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_alter_serviceprovider_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicerequest',
            options={'ordering': ['Timestamp'], 'verbose_name': 'Requested Services', 'verbose_name_plural': 'Requested Services'},
        ),
    ]
