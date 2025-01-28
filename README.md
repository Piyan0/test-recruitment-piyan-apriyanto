# **Website CRUD Sederhana**


## Instalasi
Buat virtual enviroment python dan aktifkan enviroment
```
$ python -m venv myenv
```
_Windows_

```console
$ source myenv\Scripts\activate.bat
```

_Unix atau MacOs_

```console
$ source myenv/bin/activate
```

Install depedensi ( Berapa di directory projek)
```console
$ pip install -r requirements.txt
```

Jalankan server ( Berada di directory project)

```console
$ python manage.py runserver
```

# Dokumentasi

### Memasukan data ke database

Dalam tahap ini, saya memasukan semua data
yang didapat dari API ke dalam database
Django, saya menggunakan database MySql.

Ini adalah custom script yang saya gunakan 
untuk memasukan data yang ada di API, ini diregistrasikan dengan nama `seed` ke manage.py, sehingga
saya bisa memanggil fungsi ini di command line untuk mengisi database.

```python
for i in self.api_data['data']:
  product_name= i["nama_produk"]
  product_price= i["harga"]
  status_id= 1 if i['status'] == 'bisa dijual' else 2
  category_id= self.category.index(i['kategori'])+1
  Product(product_name= product_name, product_price= product_price, status_id= status_id, category_id= category_id).save()
  
```

Sebelumnya saya sudah membuat Model 
Produk, Status dan Category dengan field yang 
sudah di tentukan.

### Menampilkan data ke halaman dengan filter
Untuk menampilkan data dengan filter tertentu, 
saya menggunakan query string untuk menambahkan field
`filter` yang berguna untuk pengambilan data berdasarkan filter.

```python
filter= req.GET.get('filter')
```

Setelah mendapatkan nilai dari `filter`, saya mengambil data dari database
dengan menggunakan `filter` sebagai acuan. Jika `filter` tidak 
bernilai, maka saya akan mengambil semua data yang ada. 

```python
filter = None (Menampilkan semua data yang ada)
filter = bisa-dijual (Menampilkan data dengan status bisa dijual)
filter = tidak-bisa-dijual (Menampilkan data dengan status tidak bisa dijual)
```

Pengambilan data dilakukan dengan menggunakan `Model Relationship`, model `Produk` memiliki
_foreign key_ status dan category yang nantinya bisa digunakan dalam pengambilan data
berdasarkan filter yang dipilih. Jika `filter` bernilai, maka saya akan mengambil model `Status` dan 
mengambil semua data dengan `<variabel_model_status>.product_set.all()`

```python
#id 2 adalah status tidak bisa dijual
status= Status.objects.get(id= 2)
products= status.product_set.all()
```

Setelah mendapatkan data, saya mendistribusikan pada fungsi `render()`:

```python
return render(req, "index.html", {...'products': products...})
```

Setelah itu, saya menggunakan _for loop_ di django template.

```python
{% for product in products %}
  {% include 'includes/product_card.html' %}
{% endfor %}
```

Tag `include` adalah tag bawaan dari Django, berguna untuk 
memisahkan komponen dari halaman utama, sehingga jika ada perubahan pada komponen tertentu
, kita hanya perlu mengedit file komponennya.


### Fitur Tambah Dan Edit

Dalam fitur tambah, saya membuat form 
dengan field yang sama dengan model `Produk`, field yang 
saya tambahkan yaitu `name, price, category dan status.`

```python
Product(
  product_name= name,
  product_price= price,
  category_id= category_id,
  status_id= status_id
  ).save()
```

Menggunakan method save() untuk menyimpan di 
database.

Untuk fitur edit, saya menggunakan form yang sama, namun field yang ada 
di form sudah diisi dengan data produk yang dipilih.

### Fitur Hapus

Untuk fitur hapus, saya menggunakan id produk 
yang nantinya digunakan untuk melakukan penghapusan dari database. Tapi, 
sebelum data dihapus, akan ada pop up konfirmasi yang harus dipilih user.

Untuk pop up nya, saya menggunakan javascript untuk memunculkan dan menyembunyikan
popup.

```python
function request_deletion(product_id):
...
url.attributes.href.value= '/product-delete?product-id='+product_id
...
```

Seperti yang bisa dilihat dari snippet kode diatas,
saya mengubah value href `<a>` dengan `product_id` yang merupakan sebuah parameter. 
`<a>` dalam hal ini adalah opsi pada popup node, dengan teks 'Hapus'.


Jadi, setiap fungsi itu dipanggil, maka url penghapusan akan berubah sesuai dengan parameter 
`product_id`.

Saya menempatkan sebuah `<p>` dengan teks `Hapus` di setiap produk yang ditampilkan dan menetapkan 
event `onclick` dengan fungsi `request_deletion`, untuk parameternya, saya mendistribusikan id setiap produk. Id didapatkan 
dari _for loop_ saat menampilkan halaman.

```python
{% for product in products %}
...
<p class="no-deco clickable text-muted" onclick="request_deletion({{product.id}})">Hapus</p>
...
{% endfor %}
```

## Framework yang digunakan

### Django
Untuk Front-End dan Back-End.

### Bootstrap 5
Untuk styling menggunakan class.

## Lainnya

Nama **Piyan Apriyanto**\
No. Hp **0838 6909 4141**\
Email **piyanapriyanto.0@gmail.com**





