# Generated by Django 3.2.9 on 2021-12-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcm_app', '0005_auto_20211208_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_email',
            field=models.EmailField(max_length=100),
        ),
    ]
