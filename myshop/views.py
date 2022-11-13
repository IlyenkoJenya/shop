from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.utils.datetime_safe import datetime

from .form import FbForm
from .models import Category, Product
from cart.forms import CartAddProductForm
import telebot

bot = telebot.TeleBot('5581275291:AAEm8omhP6a3Em9KKlpv79vwqeH3K-gd3XQ')
chatId = '-876303158'


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    categories = Category.objects.all()
    return render(request, 'shop/product/detail.html',
                  {'product': product, 'cart_product_form': cart_product_form, 'categories': categories, })


def index(request):
    return render(request, 'shop/product/index.html')


def delivery(request):
    return render(request, 'shop/product/delivery.html')


def contact(request):
    return render(request, 'shop/product/contact.html')


def fb(request):
    if request.method == "POST":
        form = FbForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = datetime.now().strftime("%d.%m.%Y %H:%M")
            x=str(post.created_at)
            post.save()
            bot.send_message(chatId,f' '+ '<b>'+"Заявка на звонок ☎"+'</b>'+
                             '\n\n'+'Имя:  '+ post.name +
                             '\n'+'Телефон:  ' + post.phone +
                             '\n'+'Время заявки:  ' + x, parse_mode='html')

            messages.add_message(request, messages.SUCCESS, 'Заявка добавлена')
            return render(request, 'shop/product/index.html')
        else:
            form = FbForm()
            messages.add_message(request, messages.WARNING, 'Заявка не отправлена.Укажите корректно номер телефона.')
            return render(request, 'shop/product/fb.html', {'form': form})
    else:
        form = FbForm()
        return render(request, 'shop/product/fb.html', {'form': form})
