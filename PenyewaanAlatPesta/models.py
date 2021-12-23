from django.db import models

# Create your models here.

class AlatPesta(models.Model):
    AlatPestaId = models.AutoField(primary_key=True)
    AlatPestaNama = models.CharField(max_length=100)

class Transaksi(models.Model):
    TransaksiId = models.AutoField(primary_key=True)
    TransaksiPembeliId = models.IntegerField(default=0)
    TransaksiTanggal = models.DateField()
    TransaksiNama = models.CharField(max_length=100)
    TransaksiJumlah = models.IntegerField(default=0)
    TransaksiTotal = models.IntegerField(default=0)

class Pembeli(models.Model):
    PembeliId = models.AutoField(primary_key=True)
    PembeliNama = models.CharField(max_length=200)
    PembeliGender = models.CharField(max_length=10)
    PembeliAlamat = models.CharField(max_length=200)