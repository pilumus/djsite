from .models import Good, Stock
from django.shortcuts import render, redirect

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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


def indexView(request):
    return render(request, 'index.html')
@login_required()

def dashboardView(request):
    return render(request, "dashboard.html")

# def loginView(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login_url')


def registerView(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('dfshop:home')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request,
                          template_name='registration/register.html',
                          context={"form": form})

    form = UserCreationForm()
    return render(request,
                  template_name='registration/register.html',
                  context={"form": form})

# Create your views here.
