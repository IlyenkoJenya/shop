from datetime import datetime

import telebot
from cart.cart import Cart
from django.shortcuts import render

from .forms import OrderCreateForm
from .models import OrderItem

bot = telebot.TeleBot('5581275291:AAEm8omhP6a3Em9KKlpv79vwqeH3K-gd3XQ')
chatId = '-876303158'


# Create your views here.


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         )
                x = str(datetime.now().strftime("%d.%m.%Y %H:%M"))
                z = str(order.id)
                bot.send_message(chatId, f' ' + '<b>' + "Заказ 💰" + '</b>' +
                                 '\n\n' + 'Имя:  ' + order.first_name +
                                 '\n' + 'Телефон:  ' + order.postal_code +
                                 '\n' + 'Время заявки:  ' + str(datetime.now().strftime("%d.%m.%Y %H:%M")) +
                                 '\n' + 'Номер заказа:  ' + str(order.id) + '\n\n' +
                                 '\n' + 'Товар:  ' + '<b>' + str(item['product']) + '</b>' +
                                 "\n" + 'Цена за 1шт.:  ' + str(item['price']) + '\n\n' +
                                 "\n" + 'Количество единиц товара:  ' + '<b>' + str(item['quantity']) + '</b>' +
                                 "\n" + 'Общая стоимость:  ' + '<b>' + str(item['total_price']) + '</b>',
                                 parse_mode='html')
                # clear the cart

            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})
