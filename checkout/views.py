from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart!")
        return redirect(reverse('products'))
        
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PQrw2CBk1oXddjNZbJY3OSdzDPqeyG8tbtnGPbEAycoFXthzyCop1B8aZ1NXBMBM3UA3DC5srDEERPrSETv7KnK00H3PL4kSt',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)