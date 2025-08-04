from django.shortcuts import render

# Create your views here.





def index(request):
    
    ctx={}
    return render(request,'site/pages/index.html', ctx)



def cart(request):
    
    ctx={}
    return render(request,'site/pages/cart.html', ctx)





def catalog(request):
    
    ctx={}
    return render(request,'site/pages/catalog.html', ctx)






def compare(request):
    
    ctx={}
    return render(request,'site/pages/compare.html', ctx)







def product(request):
    
    ctx={}
    return render(request,'site/pages/product.html', ctx)



def contacts(request):
    
    ctx={}
    return render(request,'site/pages/contacts.html', ctx)


