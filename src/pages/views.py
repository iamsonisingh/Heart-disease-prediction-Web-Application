from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {}) #string of html code

def user_heart_info_view(request, *args, **kwargs):
    return render(request, 'user_heart_info.html', {})

# def user_heart_info_view(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         print(email)
#     context = {}
#     return render(request, "user_heart_info.html", {})

# def product_detail_view(request):
#     obj = predictionInfo.objects.get(id=1)
#     # context = {
#     #     'age': obj.age,
#     #     'sex': obj.sex
#     # }
#     context = {
#          'object': obj
#      }
#     return render(request, "detail.html", context)

def prediction_page_view(request, *args, **kwargs):
    if request.method == 'POST':
        values = request.POST
        values.save()

    context = {

            'object': values
        }
    return render(request, 'prediction_page.html', context)

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def footer_view(request, *args, **kwargs):
    return render(request, 'footer.html', {})

def login_view(request, *args, **kwargs):
    return render(request, 'login.html', {})