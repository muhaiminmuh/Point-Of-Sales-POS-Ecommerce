from django.db import models
from master.models import *

# Create your models here.

class Penjualan(models.Model) :
	operator = models.ForeignKey(Operator, on_delete = models.PROTECT)
	kategori = models.ForeignKey(KategoriBarang, on_delete = models.PROTECT)
	brand = models.ForeignKey(Brand, on_delete = models.PROTECT)
	barang = models.ForeignKey(Barang, on_delete = models.PROTECT)
	jumlah = models.IntegerField()
	tanggal = models.DateField()

	def __str__(self):
		return self.operator.nama + " - " + self.kategori.nama_kategori + " - " + self.brand.nama_brand + " - " + self.barang.nama_barang

class Pembelian(models.Model) :
	supplier = models.ForeignKey(Supplier, on_delete = models.PROTECT)
	kategori = models.ForeignKey(KategoriBarang, on_delete = models.PROTECT)
	brand = models.ForeignKey(Brand, on_delete = models.PROTECT)
	barang = models.ForeignKey(Barang, on_delete = models.PROTECT)
	jumlah = models.IntegerField()
	tanggal = models.DateField()

	def __str__(self):
		return self.supplier.nama_supplier + " - " + self.kategori.nama_kategori + " - " + self.brand.nama_brand + " - " + self.barang.nama_barang
