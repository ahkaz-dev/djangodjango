from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm

def cataloges(request):
    if request.method == "POST":
            name = request.POST.get("name")
            number = request.POST.get("number")
            # return HttpResponse(f"<h2>Данные отправлены, {name}, ваш номер: {number}</h2>")
            print(name, number)
            return render(request, "contacts.html", {"form": "Данные были отправлены"})
    else:
            userform = UserForm()
            return render(request, "contacts.html", {"form": userform})