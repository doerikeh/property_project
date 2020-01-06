from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contact.models import Contact

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'USername Sudah Ada')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email Sudah Ada')
                    return redirect('accounts:register')
                else: 
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name
                    =last_name)

                    # auth.login(request, user)
                    # messages.success(request, "selamat anda sudah membuat akun baru")
                    # return redirect("pages:index")
                    user.save()
                    messages.success(request, "selamat anda sudah membuat akun baru")
                    return redirect('accounts:login')
        else:
            messages.error(request, 'password do not match')
            return redirect('accounts:register')
    else:
        return render (request, "accounts/register.html", {})   

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'selamat anda sudah login')
            return redirect("accounts:dashboard")
        else:
            messages.error(request, "anda gagal login")
            return redirect("accounts:login")
    else:
        return render (request, "accounts/login.html", {})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "selamat anda sudah logout")
        return redirect("pages:index")

def dashboard(request):
    user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contact
    }
    return render (request, "accounts/dashboard.html", context)