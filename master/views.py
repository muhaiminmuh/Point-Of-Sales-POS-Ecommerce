from django.shortcuts import render
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle 
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle 
from reportlab.lib.units import inch 
from reportlab.lib.pagesizes import A4, landscape 
from reportlab.lib import colors 
from django.http import HttpResponse
import json

#import semua class dari master.models 
from master.models import * 
from transaction.models import *
 

# Create your views here.
def cetak_kategoribarang(request):
	# pengaturan respon berformat pdf
	namaFile = "Lap_Kategori_Muhaimin.pdf"
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="' + namaFile + '"'

    # mengambil data mahasiswa
	data = KategoriBarang.objects.all()

    #membuat variabel table_data yang digunakan untuk mengisi tabel
	table_data = []

    #membuat judul/header tabel
	table_data.append([ "ID Kategori", "Nama Kategori" ])

    #mengisi tabel
    #nama field disesuaikan dengan class Mahasiswa yang ada di dalam master
	for item in data:
		table_data.append([ item.kategori_id, item.nama_kategori ])

    # membuat dokumen baru
	doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=5, leftMargin=5, topMargin=5, bottomMargin=5)
	styles = getSampleStyleSheet()

    # pengaturan tabel di pdf
	table_style = TableStyle([
    							('ALIGN',(1,1),(-2,-2),'RIGHT'),
     							('VALIGN',(0,0),(0,-1),'TOP'),
     							('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
     							('BOX', (0,0), (-1,-1), 0.25, colors.black),
                        ])

    #Membuat Tabel dengan isi table_data
	mahasiswa_table = Table(table_data)
	mahasiswa_table.setStyle(table_style)

    # mengisi konten pdf
	konten = []
	konten.append(Paragraph('LAPORAN KATEGORI BARANG', styles['Title']))
	konten.append(Spacer(1,12))
	konten.append(mahasiswa_table)

    # menghasilkan/generate pdf untuk diunduh
	doc.build(konten)

	return response

def cetak_brand(request):
	# pengaturan respon berformat pdf
	namaFile = "Lap_Brand_Muhaimin.pdf"
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="' + namaFile + '"'

    # mengambil data mahasiswa
	data = Brand.objects.all()

    #membuat variabel table_data yang digunakan untuk mengisi tabel
	table_data = []

    #membuat judul/header tabel
	table_data.append([ "ID Brand", "Nama Brand" ])

    #mengisi tabel
    #nama field disesuaikan dengan class Mahasiswa yang ada di dalam master
	for item in data:
		table_data.append([ item.brand_id, item.nama_brand ])

    # membuat dokumen baru
	doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=5, leftMargin=5, topMargin=5, bottomMargin=5)
	styles = getSampleStyleSheet()

    # pengaturan tabel di pdf
	table_style = TableStyle([
    							('ALIGN',(1,1),(-2,-2),'RIGHT'),
     							('VALIGN',(0,0),(0,-1),'TOP'),
     							('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
     							('BOX', (0,0), (-1,-1), 0.25, colors.black),
                        ])

    #Membuat Tabel dengan isi table_data
	mahasiswa_table = Table(table_data)
	mahasiswa_table.setStyle(table_style)

    # mengisi konten pdf
	konten = []
	konten.append(Paragraph('LAPORAN BRAND BARANG', styles['Title']))
	konten.append(Spacer(1,12))
	konten.append(mahasiswa_table)

    # menghasilkan/generate pdf untuk diunduh
	doc.build(konten)

	return response

def cetak_supplier(request):
	# pengaturan respon berformat pdf
	namaFile = "Lap_Supplier_Muhaimin.pdf"
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="' + namaFile + '"'

    # mengambil data mahasiswa
	data = Supplier.objects.all()

    #membuat variabel table_data yang digunakan untuk mengisi tabel
	table_data = []

    #membuat judul/header tabel
	table_data.append([ "Kode Supplier", "Nama Supplier", "Alamat", "No Telepon" ])

    #mengisi tabel
    #nama field disesuaikan dengan class Mahasiswa yang ada di dalam master
	for item in data:
		table_data.append([ item.kode_supplier, item.nama_supplier, item.alamat, item.no_telepon ])

    # membuat dokumen baru
	doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=5, leftMargin=5, topMargin=5, bottomMargin=5)
	styles = getSampleStyleSheet()

    # pengaturan tabel di pdf
	table_style = TableStyle([
    							('ALIGN',(1,1),(-2,-2),'RIGHT'),
     							('VALIGN',(0,0),(0,-1),'TOP'),
     							('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
     							('BOX', (0,0), (-1,-1), 0.25, colors.black),
                        ])

    #Membuat Tabel dengan isi table_data
	mahasiswa_table = Table(table_data)
	mahasiswa_table.setStyle(table_style)

    # mengisi konten pdf
	konten = []
	konten.append(Paragraph('LAPORAN SUPPLIER BARANG', styles['Title']))
	konten.append(Spacer(1,12))
	konten.append(mahasiswa_table)

    # menghasilkan/generate pdf untuk diunduh
	doc.build(konten)

	return response

def cetak_operator(request):
	# pengaturan respon berformat pdf
	namaFile = "Lap_Operator_Muhaimin.pdf"
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="' + namaFile + '"'

    # mengambil data mahasiswa
	data = Operator.objects.all()

    #membuat variabel table_data yang digunakan untuk mengisi tabel
	table_data = []

    #membuat judul/header tabel
	table_data.append([ "ID Operator", "Nama", "Alamat", "Jenis Kelamin", "No Telepon", "Email" ])

    #mengisi tabel
    #nama field disesuaikan dengan class Mahasiswa yang ada di dalam master
	for item in data:
		table_data.append([ item.id_operator, item.nama, item.alamat, item.jenis_kelamin, item.no_telepon, item.email ])

    # membuat dokumen baru
	doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=5, leftMargin=5, topMargin=5, bottomMargin=5)
	styles = getSampleStyleSheet()

    # pengaturan tabel di pdf
	table_style = TableStyle([
    							('ALIGN',(1,1),(-2,-2),'RIGHT'),
     							('VALIGN',(0,0),(0,-1),'TOP'),
     							('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
     							('BOX', (0,0), (-1,-1), 0.25, colors.black),
                        ])

    #Membuat Tabel dengan isi table_data
	mahasiswa_table = Table(table_data)
	mahasiswa_table.setStyle(table_style)

    # mengisi konten pdf
	konten = []
	konten.append(Paragraph('LAPORAN OPERATOR', styles['Title']))
	konten.append(Spacer(1,12))
	konten.append(mahasiswa_table)

    # menghasilkan/generate pdf untuk diunduh
	doc.build(konten)

	return response

def cetak_barang(request):
	# pengaturan respon berformat pdf
	namaFile = "Lap_Barang_Muhaimin.pdf"
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="' + namaFile + '"'

    # mengambil data mahasiswa
	data = Barang.objects.all()

    #membuat variabel table_data yang digunakan untuk mengisi tabel
	table_data = []

    #membuat judul/header tabel
	table_data.append([ "ID Barang", "Kategori", "Brand", "Nama Barang", "Harga" ])

    #mengisi tabel
    #nama field disesuaikan dengan class Mahasiswa yang ada di dalam master
	for item in data:
		table_data.append([ item.barang_id, item.kategori, item.brand, item.nama_barang, item.harga ])

    # membuat dokumen baru
	doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=5, leftMargin=5, topMargin=5, bottomMargin=5)
	styles = getSampleStyleSheet()

    # pengaturan tabel di pdf
	table_style = TableStyle([
    							('ALIGN',(1,1),(-2,-2),'RIGHT'),
     							('VALIGN',(0,0),(0,-1),'TOP'),
     							('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
     							('BOX', (0,0), (-1,-1), 0.25, colors.black),
                        ])

    #Membuat Tabel dengan isi table_data
	mahasiswa_table = Table(table_data)
	mahasiswa_table.setStyle(table_style)

    # mengisi konten pdf
	konten = []
	konten.append(Paragraph('LAPORAN BARANG', styles['Title']))
	konten.append(Spacer(1,12))
	konten.append(mahasiswa_table)

    # menghasilkan/generate pdf untuk diunduh
	doc.build(konten)

	return response

def grafik_operator(request) :

	#ambil data mahasiswa
	dataMahasiswa = Operator.objects.all();

	#membuat data grafik
	data_grafik = []


	#ambil jumlah mahasiswa dengan filter jenis kelamin = 'L'
	jmlLaki2 = dataMahasiswa.filter(jenis_kelamin='L'). count()
	data_grafik.append({"name" : "Laki-laki", "y":jmlLaki2})

	#ambil jumlah mahasiswa dengan filter jenis kelamin = 'P'
	jmlPerempuan = dataMahasiswa.filter(jenis_kelamin='P'). count()
	data_grafik.append({"name" : "Perempuan", "y":jmlPerempuan})

	#tampilkan data_grafik dalam format json
	json_grafik = json.dumps(data_grafik)

	#tampilkan file template grafik_mahasiswa.html dengan membawa nilai json_grafik
	return render(request,'grafik_operator.html',{'json_grafik':json_grafik})

def grafik_barang(request) :

	#ambil data mahasiswa
	dataMahasiswa = Barang.objects.all();

	#membuat data grafik
	data_grafik = []


	#ambil jumlah mahasiswa dengan filter jenis kelamin = 'L'
	jmlMouse = dataMahasiswa.filter(kategori_id='K01'). count()
	data_grafik.append({"name" : "Mouse", "y":jmlMouse})

	#ambil jumlah mahasiswa dengan filter jenis kelamin = 'P'
	jmlKeyboard = dataMahasiswa.filter(kategori_id='K02'). count()
	data_grafik.append({"name" : "Keyboard", "y":jmlKeyboard})

	jmlLaptop = dataMahasiswa.filter(kategori_id='K03'). count()
	data_grafik.append({"name" : "Laptop", "y":jmlLaptop})

	jmlHeadphone = dataMahasiswa.filter(kategori_id='K04'). count()
	data_grafik.append({"name" : "Headphone", "y":jmlHeadphone})

	#tampilkan data_grafik dalam format json
	json_grafik = json.dumps(data_grafik)

	#tampilkan file template grafik_mahasiswa.html dengan membawa nilai json_grafik
	return render(request,'grafik_barang.html',{'json_grafik':json_grafik})

def grafik_supplier(request) :

	#ambil data mahasiswa
	dataMahasiswa = Supplier.objects.all();

	#membuat data grafik
	data_grafik = []


	#ambil jumlah mahasiswa dengan filter jenis kelamin = 'L'
	jmlKodeS01 = dataMahasiswa.filter(kode_supplier='S01'). count()
	data_grafik.append({"name" : "PT. Computer Market", "y":jmlKodeS01})

	#ambil jumlah mahasiswa dengan filter jenis kelamin = 'P'
	jmlKodeS02 = dataMahasiswa.filter(kode_supplier='S02'). count()
	data_grafik.append({"name" : "Digital Computer", "y":jmlKodeS02})

	jmlKodeS05 = dataMahasiswa.filter(kode_supplier='S05'). count()
	data_grafik.append({"name" : "PT. Laptop Murah", "y":jmlKodeS05})

	#tampilkan data_grafik dalam format json
	json_grafik = json.dumps(data_grafik)

	#tampilkan file template grafik_mahasiswa.html dengan membawa nilai json_grafik
	return render(request,'grafik_supplier.html',{'json_grafik':json_grafik})

def list_kategori(request):
	datane = KategoriBarang.objects.all()
	return render(request, "kategori.html", {"data" : datane})

def list_barang(request):
	datane = Barang.objects.all()
	return render(request, "barang.html", {"data" : datane})

def list_brand(request):
	datane = Brand.objects.all()
	return render(request, "brand.html", {"data" : datane})

def list_operator(request):
	datane = Operator.objects.all()
	return render(request, "operator.html", {"data" : datane})