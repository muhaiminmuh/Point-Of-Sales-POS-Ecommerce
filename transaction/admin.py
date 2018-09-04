from django.contrib import admin
from transaction.models import *

class PenjualanAdmin (admin.ModelAdmin):
	list_display = ['operator', 'kategori', 'brand', 'barang', 'jumlah', 'tanggal']
	list_filter = ('operator', 'kategori', 'brand')
	search_field = []
	list_per_page = 20

admin.site.register(Penjualan, PenjualanAdmin)

class PembelianAdmin (admin.ModelAdmin):
	list_display = ['supplier', 'kategori', 'brand', 'barang', 'jumlah', 'tanggal']
	list_filter = ('supplier', 'kategori', 'brand')
	search_field = []
	list_per_page = 20

admin.site.register(Pembelian, PembelianAdmin)