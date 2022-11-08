from .models import Good, Stock
from django.shortcuts import render
from django.http import HttpResponse

def goods(request):
    goods_list = Good.objects.all() #QuerySet
    stock = Stock.objects.all()
    context = {'goods_list': goods_list,
               'stock': stock}
    return render(request, 'dfshop/goods.html', context)

def good_details(request, good):
    return HttpResponse("You're looking at %s." % good)

# Create your views here.
