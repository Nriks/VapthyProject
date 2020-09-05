from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from home.models import Company, Product


def home(request):
    return render(request, 'home.html')


def afficherCompany(request):
    companies = Company.objects.all()
    return render(request, 'companies.html', {'all_companies': companies})
    
def showAllProducts(request):
    products = Product.objects.all()
    return render(request, 'allProducts.html', {'all_products': products})


# def afficherCompany(request):
#     return render(request, 'companies.html')

def companyPage(request, id):
    company = get_object_or_404(Company, id=id)
    # product = get_object_or_404(Product, company_id = id)
    product = Product.objects.filter(company_id = id)
    # product = Product.objects.filter(company_id = id)
    return render(request, 'companyPage.html', {'company': company, 'product': product})

# def companyProducts(request, id):
#     product = get_object_or_404(Product, id=id)
#     return render(request, 'companyPage.html', {"all_Articles_Company": product})

def detailsProduct(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detailsProduct.html', {'product': product})