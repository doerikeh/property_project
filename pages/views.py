from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by("-list_update").filter(is_published=True)[:3]
    context = {
        "listings": listings,
        'state_choice': state_choices,
        'bedroom': bedroom_choices,
        'price': price_choices
    }
    return render(request, "pages/index.html", context)

def about(request):
    realtor = Realtor.objects.order_by("-hire_date")
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtor,
        'mvp_realtor': mvp_realtors
    }
    return render(request, "pages/about.html", context)
