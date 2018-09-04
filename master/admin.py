from django.contrib import admin
from master.models import *

# Register your models here.
class OperatorAdmin (admin.ModelAdmin) :
    list_display = ['id_operator','nama','alamat','jenis_kelamin','no_telepon','email']
    list_filter = ('alamat','jenis_kelamin')
    search_fields = ['id_operator','nama']
    list_per_page = 20

admin.site.register(Operator, OperatorAdmin)

class KategoriBarangAdmin (admin.ModelAdmin) :
    list_display = ['kategori_id', 'nama_kategori']
    list_filter = ()
    search_fields = ['kategori_id', 'nama_kategori']
    list_per_page = 20

admin.site.register(KategoriBarang, KategoriBarangAdmin)

class BrandAdmin (admin.ModelAdmin) :
    list_display = ['brand_id', 'nama_brand']
    list_filter = ()
    search_fields = ['brand_id', 'nama_brand']
    list_per_page = 20

admin.site.register(Brand, BrandAdmin)

class BarangAdmin (admin.ModelAdmin) :
    list_display = ['barang_id', 'kategori', 'brand', 'nama_barang', 'file_barang', 'harga']
    list_filter = ('kategori', 'brand')
    search_fields = ['barang_id', 'kategori', 'brand', 'nama_barang']
    list_per_page = 20

admin.site.register(Barang, BarangAdmin)

class SupplierAdmin (admin.ModelAdmin) :
    list_display = ['kode_supplier', 'nama_supplier', 'alamat', 'no_telepon']
    list_filter = ()
    search_fields = ['kode_supplier', 'nama_supplier', 'alamat']
    list_per_page = 20

admin.site.register(Supplier, SupplierAdmin)
