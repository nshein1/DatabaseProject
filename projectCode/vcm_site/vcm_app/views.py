from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the VCM index.")

def vendors(request):
    return HttpResponse("Hello, world. You're at the vendors page.") 



def vendor_detail(request, vendor_id):
    return HttpResponse("You're looking at vendor %s." % vendor_id)


def contracts(request):
    return HttpResponse("Hello, world. You're at the contracts page.") 


def contract_detail(request, contract_id):
    return HttpResponse("You're looking at contract %s." % contract_id)