from django.db import models

# Create your models here.
class Operator (models.Model) :
	JK = (
			('L', 'Laki-laki'),
			('P', 'Perempuan')
	)

	id_operator = models.CharField(max_length=5, primary_key=True)
	nama = models.CharField(max_length=150)
	alamat = models.TextField()
	jenis_kelamin = models.CharField(max_length=1, choices=JK)
	no_telepon = models.CharField(max_length=30, blank=True)
	email = models.CharField(max_length=100, blank=True)

	def __str__(self) :
		return self.nama

class KategoriBarang (models.Model) :
    kategori_id = models.CharField(max_length=5, primary_key=True)
    nama_kategori = models.CharField(max_length=30)

    def __str__(self) :
        return self.nama_kategori

class Brand (models.Model) :
	brand_id= models.CharField(max_length=5, primary_key=True)
	nama_brand = models.CharField(max_length=30)

	def __str__(self) :
		return self.nama_brand

class Barang (models.Model) :
	barang_id = models.CharField(max_length=5, primary_key=True)
	kategori = models.ForeignKey(KategoriBarang, on_delete=models.PROTECT)
	brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
	nama_barang = models.CharField(max_length=50)
	file_barang = models.FileField(upload_to='tema/static/media')
	harga = models.IntegerField()

	def __str__(self) :
		return str(self.nama_barang) + " - " + str(self.kategori)

class Supplier (models.Model) :
    kode_supplier = models.CharField(max_length=10, primary_key=True)
    nama_supplier = models.CharField(max_length=50)
    alamat = models.TextField()
    no_telepon = models.CharField(max_length=30, blank=True)

    def __str__(self) :
        return self.nama_supplier
