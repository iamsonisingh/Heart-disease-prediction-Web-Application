"""heartDiseasePrediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#custom pages
from pages.views import home_view, contact_view, user_heart_info_view, about_view, footer_view, prediction_page_view, login_view

urlpatterns = [
    #create diff pages and route that here like contact etc
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('userInfo/', user_heart_info_view, name='userInfo'),
    path('about/', about_view, name='about'),
    path('footer/', footer_view, name='footer'),
    path('prediction/', prediction_page_view, name='prediction'),
    path('login/', login_view, name='login'),
    path('admin/', admin.site.urls)

]



