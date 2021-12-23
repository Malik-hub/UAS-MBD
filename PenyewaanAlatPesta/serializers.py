from django.db.models import fields
from rest_framework import serializers
from PenyewaanAlatPesta.models import AlatPesta,Transaksi,Pembeli

class AlatPestaSerializers(serializers.ModelSerializer):
    class Meta:
        model=AlatPesta
        fields=('AlatPestaId','AlatPestaNama')

class TransaksiSerializers(serializers.ModelSerializer):
    class Meta:
        model=Transaksi
        fields=('TransaksiId','TransaksiTanggal','TransaksiNama','TransaksiJumlah','TransaksiTotal')

class PembeliSerializers(serializers.ModelSerializer):
    class Meta:
        model=Pembeli
        fields=('PembeliId','PembeliNama','PembeliGender','PembeliAlamat')