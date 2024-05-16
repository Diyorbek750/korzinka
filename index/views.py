from django.shortcuts import render,get_object_or_404,redirect
from products.models import Product,Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Saved
from django.contrib import messages


# Create your views here.
def for_all_pages(request):
    categories = Category.objects.all()
    return {"categories":categories}

class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        q=request.GET.get('q', '')
        if q:
            products = products.filter(name__icontains=q)
        return render(request, "index.html", {'products':products,'q':q})
    
class CategoryView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)
        products = Product.objects.filter(category=category)
        q=request.GET.get('q', '')
        if q:
            products = products.filter(name__icontains=q)
        return render(request, "category.html", {'products':products, "category":category,'q':q}) 

def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product':product
    }
    return render(request,'detail.html',context)

class AddRemoveSavedView(LoginRequiredMixin,View):
    login_url = 'login'
    
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        saved_product = Saved.objects.filter(author=request.user,product=product)
        if saved_product:
            saved_product.delete()
            messages.info(request,'Removed')
        else:
            Saved.objects.create(author=request.user,product=product)
            messages.info(request,'Saved')
        return redirect(request.META.get('HTTP_REFERER'))

class SavedView(LoginRequiredMixin,View):
    login_url = 'login'
    
    def get(self,request):
        saveds = Saved.objects.filter(author=request.user)
        q=request.GET.get('q', '')
        if q:
            products = Product.objects.filter(name__icontains=q) 
            saveds = Saved.objects.filter(author=request.user, product__in=products)
        return render(request, 'saveds.html', {"saveds":saveds,'q':q})
    
class CategoryView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)
        products = Product.objects.filter(category=category)
        q=request.GET.get('q', '')
        if q:
            products = products.filter(name__icontains=q)
        return render(request, "category.html", {'products':products, "category":category}) 
        
