# Generated by Django 3.0.1 on 2020-01-04 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamdata', '0002_auto_20200103_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='alt_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
