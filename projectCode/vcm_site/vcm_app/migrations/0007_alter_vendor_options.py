# Generated by Django 3.2.9 on 2021-12-08 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcm_app', '0006_alter_vendor_vendor_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendor',
            options={'ordering': ['vendor_name']},
        ),
    ]
