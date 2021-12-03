from django.shortcuts import render

from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the VCM index.")

def vendors(request):
    #return HttpResponse("Hello, world. You're at the vendors page.") 

    """consider changing this to an order by
        e.g.   latest_question_list = Question.objects.order_by('-pub_date')[:5]"""
    vendor_list = Vendor.objects.all() 
    
    context = {'vendor_list': vendor_list,}
    
    return render(request, 'vcm_app/vendors.html', context)




def vendor_detail(request, vendor_id):
    return HttpResponse("You're looking at vendor %s." % vendor_id)


def contracts(request):
    return HttpResponse("Hello, world. You're at the contracts page.") 


def contract_detail(request, contract_id):
    return HttpResponse("You're looking at contract %s." % contract_id)