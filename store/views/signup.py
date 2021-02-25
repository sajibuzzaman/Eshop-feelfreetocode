from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        value = {
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email
        }
        
        customer = Customer(first_name = first_name, 
                                last_name = last_name,
                                phone = phone,
                                email = email,
                                password = password)
        error_message = self.validateCustomer(customer)
        # save
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('index')
        else:
            data = {
                'error':error_message,
                'values':value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
    # validation
        error_message = None
        

        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'     
        elif not customer.email:
            error_message = 'Email required'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif not customer.password:
            error_message = 'Password required'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered'

        return error_message
