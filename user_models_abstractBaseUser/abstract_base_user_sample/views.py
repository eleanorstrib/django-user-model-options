from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User was created successfully.")
        else:
            return HttpResponse("There was an error.")
    else:
        form = CadenzaUserForm()

    return render(request, 'home.html', {'form': form})
