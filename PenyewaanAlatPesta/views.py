from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.relations import ManyRelatedField

from PenyewaanAlatPesta.models import AlatPesta,Transaksi,Pembeli
from PenyewaanAlatPesta.serializers import AlatPestaSerializers,TransaksiSerializers,PembeliSerializers

# Create your views here.

@csrf_exempt
def alatpestaApi(request,id=0):
    if request.method=='GET':
        alatpesta = AlatPesta.objects.all()
        alatpesta_serializer=AlatPestaSerializers(alatpesta,many=True)
        return JsonResponse(alatpesta_serializer.data,safe=False)
    elif request.method=='POST':
        alatpesta_data=JSONParser().parse(request)
        alatpesta_serializer=AlatPestaSerializers(data=alatpesta_data)
        if alatpesta_serializer.is_valid():
            alatpesta_serializer.save()
            return JsonResponse("Berhasil Ditambahkan",safe=False)
        return JsonResponse("Tidak Berhasi Ditambahkan",safe=False)
    elif request.method=='PUT':
        alatpesta_data=JSONParser().parse(request)
        alatpesta=AlatPesta.objects.get(AlatPestaId=alatpesta_data['AlatPestaId'])
        alatpesta_serializer=AlatPestaSerializers(alatpesta,data=alatpesta_data)
        if alatpesta_serializer.is_valid():
            alatpesta_serializer.save()
            return JsonResponse("Berhasil Di Update",safe=False)
        return JsonResponse("Update Gagal")
    elif request.method=='DELETE':
        alatpesta=AlatPesta.objects.get(AlatPestaId=id)
        alatpesta.delete()
        return JsonResponse("Berhasil Dihapus",safe=False)

@csrf_exempt
def transaksiApi(request,id=0):
    if request.method=='GET':
        transaksi = Transaksi.objects.all()
        transaksi_serializer=TransaksiSerializers(transaksi,many=True)
        return JsonResponse(transaksi_serializer.data,safe=False)
    elif request.method=='POST':
        transaksi_data=JSONParser().parse(request)
        transaksi_serializer=TransaksiSerializers(data=transaksi_data)
        if transaksi_serializer.is_valid():
            transaksi_serializer.save()
            return JsonResponse("Berhasil Ditambahkan",safe=False)
        return JsonResponse("Tidak Berhasi Ditambahkan",safe=False)
    elif request.method=='PUT':
        transaksi_data=JSONParser().parse(request)
        transaksi=Transaksi.objects.get(TransaksiId=transaksi_data['TransaksiId'])
        transaksi_serializer=TransaksiSerializers(transaksi,data=transaksi_data)
        if transaksi_serializer.is_valid():
            transaksi_serializer.save()
            return JsonResponse("Berhasil Di Update",safe=False)
        return JsonResponse("Update Gagal")
    elif request.method=='DELETE':
        transaksi=Transaksi.objects.get(TransaksiId=id)
        transaksi.delete()
        return JsonResponse("Berhasil Dihapus",safe=False)

@csrf_exempt
def pembeliApi(request,id=0):
    if request.method=='GET':
        pembeli = Pembeli.objects.all()
        pembeli_serializer=PembeliSerializers(pembeli,many=True)
        return JsonResponse(pembeli_serializer.data,safe=False)
    elif request.method=='POST':
        pembeli_data=JSONParser().parse(request)
        pembeli_serializer=PembeliSerializers(data=pembeli_data)
        if pembeli_serializer.is_valid():
            pembeli_serializer.save()
            return JsonResponse("Berhasil Ditambahkan",safe=False)
        return JsonResponse("Tidak Berhasi Ditambahkan",safe=False)
    elif request.method=='PUT':
        pembeli_data=JSONParser().parse(request)
        pembeli=Pembeli.objects.get(PembeliId=pembeli_data['PembeliId'])
        pembeli_serializer=PembeliSerializers(pembeli,data=pembeli_data)
        if pembeli_serializer.is_valid():
            pembeli_serializer.save()
            return JsonResponse("Berhasil Di Update",safe=False)
        return JsonResponse("Update Gagal")
    elif request.method=='DELETE':
        pembeli=Pembeli.objects.get(PembeliId=id)
        pembeli.delete()
        return JsonResponse("Berhasil Dihapus",safe=False)