from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing     = request.POST.get('listing', 'alamat tidak di temukan')
        name    = request.POST['name']
        email    = request.POST['email']
        phone    = request.POST['phone']
        message    = request.POST['message']
        user_id    = request.POST['user_id']
        realtor_email    = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contact = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contact:
                messages.error(request, 'Anda Sudah Mengirim Email')

        contact = Contact(listing=listing, listing_id=listing_id, name=name, phone=phone, message=message,
        email=email, user_id=user_id)

        contact.save()

        send_mail(
            'Property Listing',
            'There Has Been An INquiry for ' + str(listing) + '. Sign in into admin panel for more info',
            'doerikeh21@gmail.com',
            [realtor_email, 'ike@gmail.com'],
            fail_silently=True
        )

        messages.success(request, 'Kami akan mengirim email nanti')
        return redirect('/listings/'+listing_id)

