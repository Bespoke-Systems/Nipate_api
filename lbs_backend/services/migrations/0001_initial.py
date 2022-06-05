# Generated by Django 3.2.12 on 2022-06-05 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_delete_workingdays'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'ProductCategories',
                'verbose_name_plural': 'ProductCategories',
            },
        ),
        migrations.CreateModel(
            name='WorkingDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
            ],
            options={
                'verbose_name': 'Potential Working Days',
                'verbose_name_plural': 'Potential Working Days',
            },
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AgeBracket', models.CharField(blank=True, choices=[('18+', '18+'), ('All', 'All'), ('10+', '10+'), ('16+', '16+')], max_length=9, null=True)),
                ('TimeStamp', models.DateTimeField(auto_now_add=True)),
                ('GenderID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.gender')),
                ('LocationID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.townsmodel')),
                ('ProductID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.product')),
                ('UserID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Service Providers',
                'verbose_name_plural': 'Service Providers',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='CategoryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.productcategory'),
        ),
    ]