# Generated by Django 3.0.1 on 2020-01-04 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teamdata', '0004_teammiscdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammiscdata',
            old_name='def_orb_pct',
            new_name='drb_pct',
        ),
        migrations.RenameField(
            model_name='teammiscdata',
            old_name='off_orb_pct',
            new_name='orb_pct',
        ),
    ]
