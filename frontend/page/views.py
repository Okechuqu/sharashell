from django.http import HttpResponseRedirect
from django.urls import reverse
from backend.authuser.models.students import Student

from backend.images.models import Image
from .forms import StudentRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import  render, redirect

# Create your views here.


def index(request, pagename=None):
    context = {}
    if (pagename) and (pagename != 'index') and not (str(pagename)).__contains__('.html'):
        return render(request, f'{pagename}.html', context=context)
    print(request.user)

    return render(request, 'index.html', context)


def student_register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.username = user.email
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('index')
    else:
        form = StudentRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, 'Welcome Back')
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials Please Register!!!")
            return student_register(request)
    else:
        # Render the login form
        return render(request, 'index.html')



def student_add_image(request):
    if request.method == 'POST':
        image = request.POST.get("profilePhoto")
        user = Student.object.get(id=request.user.id)
        imageInstance = Image.objects.create(image=image, title=f"{user.email}")
        user.profilePhoto = imageInstance
        user.save()
