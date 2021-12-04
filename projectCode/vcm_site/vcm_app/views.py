from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the VCM index.")

def vendors(request):
    #return HttpResponse("Hello, world. You're at the vendors page.") 

    """consider changing this to an order by
        e.g.   latest_question_list = Question.objects.order_by('-pub_date')[:5]"""
    vendor_list = Vendor.objects.all() #maybe make this a get_list_or_404()
    
    context = {'vendor_list': vendor_list,}
    
    return render(request, 'vcm_app/vendors.html', context)

class VendorsView(generic.ListView):
    template_name = 'vcm_app/vendors.html'
    context_object_name = 'vendor_list'

    def get_queryset(self):
        return Vendor.objects.all()



"""
def vendor_detail(request, vendor_id):

    vendor = get_object_or_404(Vendor, pk=vendor_id)

    return render(request, 'vcm_app/vendor_detail.html', {'vendor':vendor})
    """


#vendor_detail but with a generic view
class VendorDetailView(generic.DetailView):
    model = Vendor
    template_name = 'vcm_app/vendor_detail.html'

def contracts(request):
    return HttpResponse("Hello, world. You're at the contracts page.") 

#this is a stub for now
def contract_detail(request, contract_id):
   return HttpResponse("You're looking at contract %s." % contract_id)
    

"""class ContractDetailView(generic.DetailView):
    model = Contract
    template_name = 'vcm_app/contract_detail.html'
"""


