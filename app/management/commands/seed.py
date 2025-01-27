from django.core.management.base import BaseCommand
from app.models import *

class Command(BaseCommand):
  #?id api yang di dapat dari API yang sudah berikan
  api_data= {
  "error": 0,
  "version": "220523.0.1",
  "data": [{
    "no": "7",
    "id_produk": "6",
    "nama_produk": "ALCOHOL GEL POLISH CLEANSER GP-CLN01",
    "kategori": "L QUEENLY",
    "harga": "12500",
    "status": "bisa dijual"
    }, {
    "no": "10",
    "id_produk": "9",
    "nama_produk": "ALUMUNIUM FOIL ALL IN ONE BULAT 23mm IM",
    "kategori": "L MTH AKSESORIS (IM)",
    "harga": "1000",
    "status": "bisa dijual"
    }, {
    "no": "12",
    "id_produk": "11",
    "nama_produk": "ALUMUNIUM FOIL ALL IN ONE BULAT 30mm IM",
    "kategori": "L MTH AKSESORIS (IM)",
    "harga": "1000",
    "status": "bisa dijual"
    }, {
    "no": "13",
    "id_produk": "12",
    "nama_produk": "ALUMUNIUM FOIL ALL IN ONE SHEET 250mm IM",
    "kategori": "L MTH AKSESORIS (IM)",
    "harga": "12500",
    "status": "tidak bisa dijual"
    }, {
    "no": "16",
    "id_produk": "15",
    "nama_produk": "ALUMUNIUM FOIL HDPE / PE BULAT 23mm IM",
    "kategori": "L MTH AKSESORIS (IM)",
    "harga": "12500",
    "status": "bisa dijual"
    }, {
    "no": "18",
    "id_produk": "17",
    "nama_produk": "ALUMUNIUM FOIL HDPE / PE BULAT 30mm IM",
    "kategori": "L MTH AKSESORIS (IM)",
    "harga": "1000",
    "status": "bisa dijual"
    }, {
    "no": "19",
    "id_produk": "18",
    "nama_produk": "ALUMUNIUM FOIL HDPE / PE SHEET 250mm IM",
    "kategori": "L MTH AKSESORIS (IM)",
    "harga": "13000",
    "status": "tidak bisa dijual"
    }, {
    "no": "20",
    "id_produk": "19",
    "nama_produk": "ALUMUNIUM FOIL PET SHEET 250mm IM",
    "kategori": "L MTH AKSESORIS (IM)",
    "harga": "1000",
    "status": "tidak bisa dijual"
    }, {
    "no": "23",
    "id_produk": "22",
    "nama_produk": "ARM PENDEK MODEL U",
    "kategori": "L MTH AKSESORIS (IM)",
    "harga": "13000",
    "status": "bisa dijual"
    }, {
    "no": "24",
    "id_produk": "23",
    "nama_produk": "ARM SUPPORT KECIL",
    "kategori": "L MTH TABUNG (LK)",
    "harga": "13000",
    "status": "tidak bisa dijual"
    }, {
    "no": "25",
    "id_produk": "24",
    "nama_produk": "ARM SUPPORT KOTAK PUTIH",
    "kategori": "L MTH AKSESORIS (IM)",
    "harga": "13000",
    "status": "tidak bisa dijual"
    }, {
    "no": "27",
    "id_produk": "26",
    "nama_produk": "ARM SUPPORT PENDEK POLOS",
    "kategori": "L MTH TABUNG (LK)",
    "harga": "13000",
    "status": "bisa dijual"
    }, {
    "no": "28",
    "id_produk": "27",
    "nama_produk": "ARM SUPPORT S IM",
    "kategori": "L MTH AKSESORIS (IM)",
    "harga": "1000",
    "status": "tidak bisa dijual"
    }, {
    "no": "29",
    "id_produk": "28",
    "nama_produk": "ARM SUPPORT T (IMPORT)",
    "kategori": "L MTH AKSESORIS (IM)",
    "harga": "13000",
    "status": "bisa dijual"
    }, {
    "no": "30",
    "id_produk": "29",
    "nama_produk": "ARM SUPPORT T - MODEL 1 ( LOKAL )",
    "kategori": "L MTH TABUNG (LK)",
    "harga": "10000",
    "status": "bisa dijual"
    }, {
    "no": "51",
    "id_produk": "50",
    "nama_produk": "BLACK LASER TONER FP-T3 (100gr)",
    "kategori": "L MTH AKSESORIS (IM)",
    "harga": "13000",
    "status": "tidak bisa dijual"
    }, {
    "no": "57",
    "id_produk": "56",
    "nama_produk": "BODY PRINTER CANON IP2770",
    "kategori": "SP MTH SPAREPART (LK)",
    "harga": "500",
    "status": "bisa dijual"
    }, {
    "no": "59",
    "id_produk": "58",
    "nama_produk": "BODY PRINTER T13X",
    "kategori": "SP MTH SPAREPART (LK)",
    "harga": "15000",
    "status": "bisa dijual"
    }, {
    "no": "60",
    "id_produk": "59",
    "nama_produk": "BOTOL 1000ML BLUE KHUSUS UNTUK EPSON R1800 / R800 - 4180 IM (T054920)",
    "kategori": "CI MTH TINTA LAIN (IM)",
    "harga": "10000",
    "status": "bisa dijual"
    }, {
    "no": "61",
    "id_produk": "60",
    "nama_produk": "BOTOL 1000ML CYAN KHUSUS UNTUK EPSON R1800 / R800 / R1900 / R2000 - 4120 IM (T054220)",
    "kategori": "CI MTH TINTA LAIN (IM)",
    "harga": "10000",
    "status": "tidak bisa dijual"
    }, {
    "no": "62",
    "id_produk": "61",
    "nama_produk": "BOTOL 1000ML GLOSS OPTIMIZER KHUSUS UNTUK EPSON R1800 / R800 / R1900 / R2000 / IX7000 / MG6170 - 4100 IM (T054020)",
    "kategori": "CI MTH TINTA LAIN (IM)",
    "harga": "1500",
    "status": "bisa dijual"
    }, {
    "no": "63",
    "id_produk": "62",
    "nama_produk": "BOTOL 1000ML L.LIGHT BLACK KHUSUS UNTUK EPSON 2400 - 0599 IM",
    "kategori": "CI MTH TINTA LAIN (IM)",
    "harga": "1500",
    "status": "tidak bisa dijual"
    }, {
    "no": "64",
    "id_produk": "63",
    "nama_produk": "BOTOL 1000ML LIGHT BLACK KHUSUS UNTUK EPSON 2400 - 0597 IM",
    "kategori": "CI MTH TINTA LAIN (IM)",
    "harga": "1500",
    "status": "tidak bisa dijual"
    }, {
    "no": "65",
    "id_produk": "64",
    "nama_produk": "BOTOL 1000ML MAGENTA KHUSUS UNTUK EPSON R1800 / R800 / R1900 / R2000 - 4140 IM (T054320)",
    "kategori": "CI MTH TINTA LAIN (IM)",
    "harga": "1000",
    "status": "bisa dijual"
    }, {
    "no": "66",
    "id_produk": "65",
    "nama_produk": "BOTOL 1000ML MATTE BLACK KHUSUS UNTUK EPSON R1800 / R800 / R1900 / R2000 - 3503 IM (T054820)",
    "kategori": "CI MTH TINTA LAIN (IM)",
    "harga": "1500",
    "status": "tidak bisa dijual"
    }, {
    "no": "67",
    "id_produk": "66",
    "nama_produk": "BOTOL 1000ML ORANGE KHUSUS UNTUK EPSON R1900 / R2000 IM - 4190 (T087920)",
    "kategori": "CI MTH TINTA LAIN (IM)",
    "harga": "1500",
    "status": "bisa dijual"
    }, {
    "no": "68",
    "id_produk": "67",
    "nama_produk": "BOTOL 1000ML RED KHUSUS UNTUK EPSON R1800 / R800 / R1900 / R2000 - 4170 IM (T054720)",
    "kategori": "CI MTH TINTA LAIN (IM)",
    "harga": "1000",
    "status": "tidak bisa dijual"
    }, {
    "no": "69",
    "id_produk": "68",
    "nama_produk": "BOTOL 1000ML YELLOW KHUSUS UNTUK EPSON R1800 / R800 / R1900 / R2000 - 4160 IM (T054420)",
    "kategori": "CI MTH TINTA LAIN (IM)",
    "harga": "1500",
    "status": "tidak bisa dijual"
    }, {
    "no": "71",
    "id_produk": "70",
    "nama_produk": "BOTOL KOTAK 100ML LK",
    "kategori": "L MTH AKSESORIS (LK)",
    "harga": "1000",
    "status": "bisa dijual"
    }, {
    "no": "73",
    "id_produk": "72",
    "nama_produk": "BOTOL 10ML IM",
    "kategori": "S MTH STEMPEL (IM)",
    "harga": "1000",
    "status": "tidak bisa dijual"
    }]
  }
  
  #?id kategory list yang nantinya akan di push ke database, di dapat dari get_category()
  category= ['L QUEENLY', 'L MTH AKSESORIS (IM)', 'L MTH TABUNG (LK)', 'SP MTH SPAREPART (LK)', 'CI MTH TINTA LAIN (IM)', 'L MTH AKSESORIS (LK)', 'S MTH STEMPEL (IM)']
  
  #?id isi database dengan api_data
  def seed(self):
    #seed status
    status_1= Status(status_name= "bisa dijual")
    status_2= Status(status_name= "tidak bisa dijual")
    status_1.save()
    status_2.save()
    
    #seed category
    for i in self.category:
      Category(category_name= i).save()
    
    #seed product
    for i in self.api_data['data']:
      product_name= i["nama_produk"]
      product_price= i["harga"]
      status_id= 1 if i['status'] == 'bisa dijual' else 2
      category_id= self.category.index(i['kategori'])+1
      Product(product_name= product_name, product_price= product_price, status_id= status_id, category_id= category_id).save()
  
  #?id ambil list kategory yang ada di api_data
  def get_category(self):
    cat= []
    for i in self.api_data["data"]:
      __cat= i["kategori"]
      if __cat in cat:
        continue
      
      cat.append(__cat)
    
    print(cat)
    
  def handle(self, *args, **kwarg):
    self.seed()
    