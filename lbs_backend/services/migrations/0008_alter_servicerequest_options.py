# Generated by Django 4.0.6 on 2022-07-12 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_servicerequest_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicerequest',
            options={'ordering': ['-Timestamp'], 'verbose_name': 'Requested Services', 'verbose_name_plural': 'Requested Services'},
        ),
    ]
