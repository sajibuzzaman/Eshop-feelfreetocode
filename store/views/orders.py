from django.shortcuts import render, redirect
from django.views import View
from store.models.orders import Order


class OrderView(View):
   def get(self, request):
       customer = request.session.get('customer')
       orders = Order.get_all_orders_by_customer(customer)

       return render(request, 'orders.html', {'orders': orders})