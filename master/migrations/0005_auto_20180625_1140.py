# Generated by Django 2.0.6 on 2018-06-25 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_auto_20180625_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='supplier_id',
            new_name='kode_supplier',
        ),
    ]