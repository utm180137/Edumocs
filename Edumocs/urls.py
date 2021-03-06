"""Edumocs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from contenido import views
from django.conf import settings 
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('carrito/',views.carrito, name="carrito"),
    path('catalogo/',views_registros.catalogo, name="catalogo"),
    path('cursos/', views_registros.cursos, name="Cursos"),
    path('login/',views.login, name="login"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)