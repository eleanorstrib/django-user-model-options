from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User was created successfully.")
        else:
            return HttpResponse("There was an error.")
    else:
        form = UserForm()

    return render (request, 'one_to_one_sample/home.html', {'form': form})
