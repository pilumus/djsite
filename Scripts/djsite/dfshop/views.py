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
    """
    good - good string from goods template.
    """
    good_split_list = good.rsplit(' ')
    good = Good.objects.get(material=good_split_list[0],
                            name__startswith=good_split_list[1]) #It should get a particular ID
    stock = Stock.objects.get(id=good.id)
    context = {'good': good,
                'stock': stock}
    return render(request, 'dfshop/good_details.html', context)

# Create your views here.
