from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .choices import state_choices, price_choices, bedroom_choices

def listings(request):
    listings = Listing.objects.order_by("-list_update").filter(is_published=True)

    page = request.GET.get('page', 9)
    paginator = Paginator(listings, 9)
    page_listing = paginator.get_page(page)
    context = {
        'listings': page_listing
    }
    return render(request, "listings/listings.html", context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        "listing": listing
    }
    return render(request, "listings/listing.html", context)

def search(request):
    queryset = Listing.objects.order_by("list_update")

    if "keywords" in request.GET:
        keyword = request.GET['keywords']
        if keyword:
            queryset = queryset.filter(description__icontains=keyword)
    
    if "city" in request.GET:
        city = request.GET['city']
        if city:
            queryset = queryset.filter(city__iexact=city)


    if "state" in request.GET:
        state = request.GET['state']
        if state:
            queryset = queryset.filter(state__iexact=state)

    if "bedrooms" in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset = queryset.filter(bedrooms__lte=bedrooms)
    
    if "price" in request.GET:
        price = request.GET['price']
        if price:
            queryset = queryset.filter(price__lte=price)

    
    context = {
        'state_choice': state_choices,
        'price_choice': price_choices,
        'bedroom_choice': bedroom_choices,
        'listings': queryset
    }
    return render(request, "listings/search.html", context)