# Generated by Django 3.2.6 on 2021-08-29 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('users', '0002_auto_20210829_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.location'),
        ),
    ]
