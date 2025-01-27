from django.shortcuts import render, HttpResponseRedirect
from .models import *
# Create your views here.
def index(req):
  
  products= Product.objects.all()
  filter= req.GET.get('filter')
  
  if filter== 'bisa-dijual':
    #?id status id 1 = bisa dijual
    status= Status.objects.get(id= 1)
    products= status.product_set.all()
    filter= "Bisa Dijual"
  
  elif filter== "tidak-bisa-dijual":
    #?id status id 2 = bisa dijual
    status= Status.objects.get(id= 2)
    products= status.product_set.all()
    filter= "Tidak Bisa Dijual"
  
  else:
    filter= "Semua"
  
  products= products.order_by('-id')
  return render(req, "index.html", {'products': products, 'filter': filter})

def delete_product(req):
  product_id= req.GET['product-id']
  target= Product.objects.get(id=product_id).delete()
  return HttpResponseRedirect('/')
  
def product_management(req, product_id):
  target_product= None
  button_text= 'Buat Produk'
  current_product= {
    'name': '',
    'price': '',
    'status_id': -1,
    'category_id': -1
  }
  
  if product_id != 0:
    target_product= Product.objects.get(id= product_id)
    current_product['name']= target_product.product_name
    current_product['price']= target_product.product_price
    current_product['category_id']= target_product.category_id
    current_product['status_id']= target_product.status_id
    
    button_text=  "Update Produk"
  
  def create_product(name, price, category_id, status_id):
    Product(product_name= name, product_price= price, category_id= category_id, status_id= status_id).save()
  
  def update_product(name, price, category_id, status_id):
    
    target_product.product_name= name
    target_product.product_price= price
    target_product.category_id= category_id
    target_product.status_id= status_id
    target_product.save()
    
  if req.method=="POST":
    data= req.POST
    name= data['name']
    price= data['price']
    category_id= int(data['category'])
    status_id= int(data['status'])
    if product_id == 0:
      create_product(name, price, category_id, status_id)
    else:
      update_product(name, price, category_id, status_id)
    
    return HttpResponseRedirect('/')
  
  category_list= Category.objects.all()
  return render(req, 'product_management.html', {'category_list': category_list, 'current_product': current_product, 'button_text' : button_text })