from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.hashers import make_password
from .models import UserData

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            age = form.cleaned_data.get('age')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            pwd = make_password(form.cleaned_data.get('password'))
            data = UserData(name,age,phone,email,pwd)
            data.save()
    else:
        form = UserForm()
    return render(request,'index.html',{'form': form})


