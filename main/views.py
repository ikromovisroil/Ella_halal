from django.shortcuts import render
from .models import *
from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import *
from django.urls import reverse
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.

def index(request):
    context = {
        'product': Product.objects.filter(status=True)[:5]
    }
    return render(request, 'main/index.html',context)


def product(request, pk=None):
    product_list = Product.objects.filter(status=True)
    if pk:
        product_list = product_list.filter(category=pk)
    context = {
        'category': Category.objects.all(),
        'product': product_list,
        'total_products': Product.objects.filter(status=True).count(),
    }
    return render(request, 'main/product.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Xabar uzatildi")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.info(request, "Yaroqsiz maʼlumot !")
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'main/contact.html',context)
