from .models import Good, Stock
from django.shortcuts import render

def goods(request):
    goods_list = Good.objects.all()
    context = {'goods_list': goods_list}
    return render(request, 'dfshop/goods.html', context)

# Create your views here.
