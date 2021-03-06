# Generated by Django 4.0 on 2021-12-23 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlatPesta',
            fields=[
                ('AlatPestaId', models.AutoField(primary_key=True, serialize=False)),
                ('AlatPestaNama', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pembeli',
            fields=[
                ('PembeliId', models.AutoField(primary_key=True, serialize=False)),
                ('PembeliNama', models.CharField(max_length=200)),
                ('PembeliGender', models.CharField(max_length=10)),
                ('PembeliAlamat', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('TransaksiId', models.AutoField(primary_key=True, serialize=False)),
                ('TransaksiTanggal', models.DateField()),
                ('TransaksiNama', models.CharField(max_length=100)),
                ('TransaksiJumlah', models.IntegerField(max_length=9)),
                ('TransaksiTotal', models.IntegerField()),
            ],
        ),
    ]
