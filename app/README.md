# **Website CRUD Sederhana**


## Instalasi
Buat virtual enviroment python dan aktifkan enviroment
```
$ python -m venv myenv
```
Install depedensi

```console
$ pip install requirement.txt
```

_Windows_

```console
$ source myenv/bin/activate
```

_Linux_

```console
$ source myenv/bin/activate
```

Jalankan server

```console
$ python manage.py runserver
```

# Dokumentasi

### Memasukan data ke database

Dalam tahap ini, saya memasukan semua data
yang ada didapat dari API ke dalam database
Django, saya menggunakan database MySql.

Ini adalah custom script yang saya gunakan 
untuk memasukan data yang ada di API.

```python
for i in self.api_data['data']:
  product_name= i["nama_produk"]
  product_price= i["harga"]
  status_id= 1 if i['status'] == 'bisa dijual' else 2
  category_id= self.category.index(i['kategori'])+1
  Product(product_name= product_name, product_price= product_price, status_id= status_id, category_id= category_id).save()
  
```

Sebelumnya saya sudah membuat Model 
produk, status dan kategory dengan field yang 
sudah di tentukan.

### Menampilkan data ke halaman dengan filter

### Fitur Tambah

### Fitur Edit

### Fitur Hapus






