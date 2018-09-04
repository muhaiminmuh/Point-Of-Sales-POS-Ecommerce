# Generated by Django 2.0.6 on 2018-06-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_barang'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('kode_supplier', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_supplier', models.CharField(max_length=50)),
                ('alamat', models.TextField()),
                ('no_telepon', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
