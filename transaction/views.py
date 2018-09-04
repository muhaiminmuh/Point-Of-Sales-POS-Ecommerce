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
def cetak_penjualan(request):
	# pengaturan respon berformat pdf
	namaFile = "Lap_Penjualan_Muhaimin.pdf"
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="' + namaFile + '"'

    # mengambil data mahasiswa
	data = Penjualan.objects.all()

    #membuat variabel table_data yang digunakan untuk mengisi tabel
	table_data = []

    #membuat judul/header tabel
	table_data.append([ "Operator", "Kategori", "Brand", "Barang", "Jumlah", "Tanggal" ])

    #mengisi tabel
    #nama field disesuaikan dengan class Mahasiswa yang ada di dalam master
	for item in data:
		table_data.append([ item.operator, item.kategori, item.brand, item.barang, item.jumlah, item.tanggal ])

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
	konten.append(Paragraph('LAPORAN PENJUALAN BARANG', styles['Title']))
	konten.append(Spacer(1,12))
	konten.append(mahasiswa_table)

    # menghasilkan/generate pdf untuk diunduh
	doc.build(konten)

	return response

def cetak_pembelian(request):
	# pengaturan respon berformat pdf
	namaFile = "Lap_Pembelian_Muhaimin.pdf"
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="' + namaFile + '"'

    # mengambil data mahasiswa
	data = Pembelian.objects.all()

    #membuat variabel table_data yang digunakan untuk mengisi tabel
	table_data = []

    #membuat judul/header tabel
	table_data.append([ "Supplier", "Kategori", "Brand", "Barang", "Jumlah", "Tanggal" ])

    #mengisi tabel
    #nama field disesuaikan dengan class Mahasiswa yang ada di dalam master
	for item in data:
		table_data.append([ item.supplier, item.kategori, item.brand, item.barang, item.jumlah, item.tanggal ])

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
	konten.append(Paragraph('LAPORAN PEMBELIAN BARANG', styles['Title']))
	konten.append(Spacer(1,12))
	konten.append(mahasiswa_table)

    # menghasilkan/generate pdf untuk diunduh
	doc.build(konten)

	return response

def grafik_pembelian(request) :

	#ambil data mahasiswa
	dataMahasiswa = Pembelian.objects.all();

	#membuat data grafik
	data_grafik = []


	#ambil jumlah mahasiswa dengan filter jenis kelamin = 'L'
	jmlKodeS01 = dataMahasiswa.filter(supplier_id='S01'). count()
	data_grafik.append({"name" : "PT. Computer Market", "y":jmlKodeS01})

	#ambil jumlah mahasiswa dengan filter jenis kelamin = 'P'
	jmlKodeS02 = dataMahasiswa.filter(supplier_id='S02'). count()
	data_grafik.append({"name" : "Digital Computer", "y":jmlKodeS02})

	jmlKodeS05 = dataMahasiswa.filter(supplier_id='S05'). count()
	data_grafik.append({"name" : "PT. Laptop Murah", "y":jmlKodeS05})

	#tampilkan data_grafik dalam format json
	json_grafik = json.dumps(data_grafik)

	#tampilkan file template grafik_mahasiswa.html dengan membawa nilai json_grafik
	return render(request,'grafik_pembelian.html',{'json_grafik':json_grafik})

def grafik_penjualan(request) :

	#ambil data mahasiswa
	dataMahasiswa = Penjualan.objects.all();

	#membuat data grafik
	data_grafik = []


	#ambil jumlah mahasiswa dengan filter jenis kelamin = 'L'
	jmlKodeK01 = dataMahasiswa.filter(kategori_id='K01'). count()
	data_grafik.append({"name" : "Mouse", "y":jmlKodeK01})

	#ambil jumlah mahasiswa dengan filter jenis kelamin = 'P'
	jmlKodeK02 = dataMahasiswa.filter(kategori_id='K02'). count()
	data_grafik.append({"name" : "Keyboard", "y":jmlKodeK02})

	jmlKodeK03 = dataMahasiswa.filter(kategori_id='K03'). count()
	data_grafik.append({"name" : "Laptop", "y":jmlKodeK03})

	jmlKodeK04 = dataMahasiswa.filter(kategori_id='K04'). count()
	data_grafik.append({"name" : "Headphone", "y":jmlKodeK04})

	#tampilkan data_grafik dalam format json
	json_grafik = json.dumps(data_grafik)

	#tampilkan file template grafik_mahasiswa.html dengan membawa nilai json_grafik
	return render(request,'grafik_penjualan.html',{'json_grafik':json_grafik})

def list_penjualan(request):
	datane = Penjualan.objects.all()
	return render(request, "penjualan.html", {"data" : datane})

def list_pembelian(request):
	datane = Pembelian.objects.all()
	return render(request, "pembelian.html", {"data" : datane})
