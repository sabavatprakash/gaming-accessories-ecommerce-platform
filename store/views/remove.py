from django.shortcuts import render, redirect
from django.views import View

from store.models.product import Products



class Remove(View):
    def post(self, request):
        remove_item = request.POST.get('product')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print( remove_item, cart, '----------------------',products,'---------remove item required--------')    
        cart.pop(remove_item)
        request.session['cart'] = cart

        return redirect('cart')
