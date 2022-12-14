from .models import Good, Stock, Wallet
from django.shortcuts import render, redirect

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def goods(request):
    goods_list = Good.objects.all() #QuerySet
    stock = Stock.objects.all()

    if request.method == 'POST':
        """ take Add to cart input of a good,
            make a new Stock line: 
                change cart_owner to logged username,
                quantity_in_stock = Add to cart input
                owner's quantity reduce on Add to cart input
        """
        user = request.user
        for good in goods_list:
            add_to_cart = request.POST.get(str(good.id))
            # print(good.id, add_to_cart)
            if add_to_cart != None:
                add_to_cart = int(add_to_cart)
                owners_good = Stock.objects.get(good=good.id, cart_owner='admin')
                try:
                    buyers_good = Stock.objects.get(good=good.id, cart_owner=user.username)
                except (KeyError, Stock.DoesNotExist):
                    buyers_good = Stock.objects.create(good=good, cart_owner=user.username)

                owners_good.quantityInStock -= add_to_cart
                buyers_good.quantityInStock += add_to_cart
                owners_good.save()
                buyers_good.save()

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
    user = request.user
    try:
        wallet = user.wallet_set.get(owner=user.id)
    except (KeyError, Wallet.DoesNotExist):
        wallet = user.wallet_set.create()

    if request.method == 'POST':
        add_gold = int(request.POST.get('number'))
        wallet.gold_quantity += add_gold
        wallet.save()

    context = {'user':user,
               'wallet':wallet}
    return render(request, "dashboard.html", context)

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

def cartView(request):
    user = request.user
    stock = Stock.objects.filter(cart_owner=user.username)

    context = {'user':user,
               'stock':stock}
    return render(request, "cart.html", context)

# Create your views here.
