# Generated by Django 3.2.9 on 2021-12-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcm_app', '0004_payment_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_email',
            field=models.EmailField(default='test@test.com', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendor_name',
            field=models.CharField(default='Sample Vendor', max_length=200),
            preserve_default=False,
        ),
    ]