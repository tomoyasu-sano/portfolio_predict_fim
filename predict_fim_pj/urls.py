"""predict_fim_pj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from predict_fim_app import views

# appnameを指定することで、この空間はdogwolfというフォルダと認識しやすく、パスが通りやすい
app_name = "predict_fim_app"

urlpatterns = [
    path("result/", views.result, name="result"),
    path("predict/", views.predict , name="predict"),
    path('admin/', admin.site.urls),
]