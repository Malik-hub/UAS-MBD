from django.urls import re_path
from PenyewaanAlatPesta import views

urlpatterns=[
    re_path(r'^alatpesta$',views.alatpestaApi),
    re_path(r'^alatpesta/([0-9]+)$',views.alatpestaApi),

    re_path(r'^transaksi$',views.transaksiApi),
    re_path(r'^transaksi/([0-9]+)$',views.transaksiApi),

    re_path(r'^pembeli$',views.pembeliApi),
    re_path(r'^pembeli/([0-9]+)$',views.pembeliApi)
]