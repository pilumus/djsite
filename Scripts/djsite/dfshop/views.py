from .models import Good, Stock
from django.shortcuts import render

def goods(request):
    goods_list = Good.objects.all() #QuerySet
    stock = Stock.objects.all()
    context = {'goods_list': goods_list,
               'stock': stock}
    return render(request, 'dfshop/goods.html', context)

# Create your views here.
