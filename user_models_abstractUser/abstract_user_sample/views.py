from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomUserForm

def home(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse("User was created successfully.")
        else:
            return HttpResponse("There was an error.")
    else:
        form = CustomUserForm()
    return render(request, 'abstract_user_sample/home.html', {'form': form})
