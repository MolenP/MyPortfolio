from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import UserForm


def user_profile_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, "main/result.html", {"data": data})
    else:
        form = UserForm()

    return render(request, "main/form.html", {"form": form})








def task_list(request):
    list = [
        "Купить молоко",
        "Помыть посуду",
        "Постирать вещи"
    ]
    context = {"list":list}
    return render(request, "main/task_list.html", context=context)






def Error404(request, exception):
    return HttpResponse("Error 404: Page is not exists")

def contact_us(request):
    return redirect("/contacts/")

def contacts(request):
    return HttpResponse("Contacts: X XXX XXX XXXX")

def JSON_view(request):
    data = {
        "name": "Yerlan",
        "age": "16"
    }
    return JsonResponse(data)

def set_cookies(request):
    response = HttpResponse("Cookies Installed")
    response.set_cookie("Username", "Yerlan")
    return response

def get_cookies(request):
    username = request.COOKIES.get("Username", "Unknown")
    return HttpResponse(f"Hello {username}!")




def articleList(request):
    sort_by = request.GET.get("sort", "name")
    return HttpResponse(f"Список статей, отсортированные по {sort_by}")

def article(request, id):
    return HttpResponse(f"Статья с ID: {id}")

def news(request):
    return HttpResponse(f"Новости")





def hello(request):
    return HttpResponse("Hello!\nAbout Us: http://127.0.0.1:8000/About_us/")

def o_nas(request):
    return HttpResponse("Меня зовут Ерлан!\nExit: http://127.0.0.1:8000")

def home(request, name, age):
    context = {
        "name": name,
        "age": age
    }

    path = request.path
    method = request.method
    user_agent = request.headers.get("User-Agent")
    host = request.get_host()

    response = HttpResponse((
        f"<p>Мое имя: {name}</p>"
        f"<p>Возраст: {age}</p>" 
        f"<p>Path: {path}</p>"
        f"<p>Method: {method}</p>"
        f"<p>User-Agent: {user_agent}</p>"
        f"<p>Host: {host}</p>"
    ))
    
    response["SecretCode"] = "315786"

    #return render(request, "main/index.html", context)
    return response

def id(request, id):
    return HttpResponse(f"Товар с ID: {id}")

