from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import YourModelForm,CartItemForm,PriceFilterForm,simpleform,newlog,otpverif,registerform
from .models import YourModel,CartItem,newform
from django.db import connection
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.http import HttpResponse
import random
import math
from django.core.mail import send_mail
def upload_image(request):
    if request.method == 'POST':
        form = YourModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Success</h1>")
            # form = form.objects.all()
            # return redirect(display)
     # Redirect to a success page
    else:
        form = YourModelForm()
    return render(request, 'upload_image.html', {'form': form})

def display(request):
    if request.method == "GET":
        product = YourModel.objects.all()
        return render(request,'product.html',{'product':product}) 

def view_cart(request):
	cart_items = CartItem.objects.filter(user=request.user)
	total_price = sum(item.product.price * item.quantity for item in cart_items)
	return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
	product = YourModel.objects.get(id=product_id)
	cart_item, created = CartItem.objects.get_or_create(product=product, 
													user=request.user)
	cart_item.quantity += 1
	cart_item.save()
	return redirect('view_cart')

def remove_from_cart(request, item_id):
	cart_item = CartItem.objects.get(id=item_id)
	cart_item.delete()
	return redirect('view_cart')

# def generate_invoice(request, cart_item_id):
#     cart_item = get_object_or_404(CartItem, id=cart_item_id)

#     # Create a response object with the appropriate MIME type for a PDF
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'inline; filename="invoice_{cart_item_id}.pdf"'

#     # Create a PDF document
#     doc = SimpleDocTemplate(response, pagesize=landscape(letter))
#     elements = []

#     # Define the data for the invoice
#     data = [
#         ["Product", "Quantity", "Price", "Total"],
#         [cart_item.product.title, cart_item.quantity, cart_item.product.price, cart_item.quantity * cart_item.product.price],
#     ]

#     # Create a table to display the invoice data
#     table = Table(data, colWidths=[200, 80, 80, 80])
#     table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#         ('GRID', (0, 0), (-1, -1), 1, colors.black),
#     ]))

#     elements.append(table)

#     # Build the PDF document
#     doc.build(elements)

#     return response

def generate_invoice(request):
    cart_items = CartItem.objects.filter(user=request.user)  # Assuming you have a cart per user

    # Calculate the total price and quantity for all cart items
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    total_quantity = sum(item.quantity for item in cart_items)

    # Create a response object with the appropriate MIME type for a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="cart_invoice.pdf"'

    # Create a PDF document
    doc = SimpleDocTemplate(response, pagesize=landscape(letter))
    elements = []

    # Define the data for the invoice
    data = [
        ["Product", "Quantity", "Price", "Total"],
    ]

    for cart_item in cart_items:
        data.append([cart_item.product.title, cart_item.quantity, cart_item.product.price, cart_item.quantity * cart_item.product.price])

    # Add a row for the total price and quantity
    data.append(["Total", total_quantity, "", total_price])

    # Create a table to display the invoice data
    table = Table(data, colWidths=[200, 80, 80, 80])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -2), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    # Build the PDF document
    doc.build(elements)

    return response

def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

global otp
otp=""    

def otpcheck(request):
    global otp
    if request.method == 'POST':
        form = otpverif(request.POST)
        if form.is_valid():
            test = form.cleaned_data
            u = test.get("otp")
            s=int(otp)
            print(otp)
            print(u)
            if u==s:
                return HttpResponseRedirect("/index")
            else:
                return HttpResponse("Invalid OTP")
    form1 = otpverif()
    context={'form':form1}
    return render(request,"otp.html",context)

def simform(request):
    global otp
    if request.method=='POST':
        s=simpleform(request.POST)
        if s.is_valid():
            data = s.cleaned_data
            modelobj=newform(firstname=data.get("fname"),lastname=data.get("lname"),password=data.get("passw"),age=data.get("age1"),email=data.get("email1"),address=data.get("address1"),phoneno=data.get("phno"),gender=data.get("gen"))
            temp_mail = data.get("email1")
            modelobj.save()
            otp = generateOTP()
            # print("HERE")
            send_mail("Verification Email","Your OTP = "+str(otp),"aryaakash1911@gmail.com",[temp_mail])
            # print("HERE")
            # f2 = otpverif()
            print("HERE")
            # return render(request,"otp.html",{'form':f2})
            return redirect('otp')

            # s.save()
            # formdata=s.cleaned_data
            # cursor=connection.cursor()
            # cursor.execute("SELECT * FROM formregister_newform WHERE email=%s;", [modelobj.email])
            # row=cursor.fetchone()
            # if row==None:
            #     modelobj.save()
            #     return HttpResponse('Success!')
            # else:
            #     return HttpResponse('Email already registered !')
        else:
            return HttpResponse('Invalid!')
    else:
        f=simpleform()
        return render(request, "simpleformdemo.html", {'form': f})

def login(request):
    if request.method=='POST':
        log=newlog(request.POST)
        if log.is_valid():
            formdata=log.cleaned_data
            email1=formdata.get("email1")
            password=formdata.get("passw")         
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM home_newform WHERE email = %s AND password = %s;", [email1, password])
            row=cursor.fetchone()
            if row==None:
                return HttpResponse('Invalid!')
            else:
                return redirect('display')
            # modelobj=newform(email=formdata.get("email1"),password=formdata.get("passw"))
            # modelobj.save()
        #     return HttpResponse('Success!')
        else:
            return HttpResponse('Invalid!')
    else:
        f=newlog()
        return render(request, "login.html", {'form': f})
