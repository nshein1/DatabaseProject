# Generated by Django 3.2.9 on 2021-12-12 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcm_app', '0015_auto_20211212_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='contract_status',
            new_name='vendor_referral',
        ),
    ]
