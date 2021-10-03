"""flipbook URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *


admin.site.site_header = "Esoteric Admin"
admin.site.site_title = "Esoteric Admin Portal"
admin.site.index_title = "Welcome to Esoteric Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/sign-up', signup, name='signup'),
    path('accounts/dashboard', dashboard, name='dashboard'),
    path('library/', bookstore, name='bookstore'),
    path('library/<int:id>/', libid, name='library'),
    path('blog/', blog, name='blog'),
    path('blog/<int:id>/', blogid, name='blogid'),
    path('cart/', cart, name='cart'),
    path('cart/<int:bid>/', cart, name='cart'),
    path('cart/<int:bid>/remove/', rcart, name='rcart'),
    path('wishlist/', wishlist, name='wishlist'),
    path('wishlist/<int:bid>/', wishlist, name='wishlist'),
    path('wishlist/<int:bid>/addcart/', wishtocart, name='wishtocart'),
    path('', index, name='index'),
    path('pages/page5/', page5, name='page5'),
    path('pages/page6/', page6, name='page6'),
    path('pages/page7/', page7, name='page7'),
    path('pages/page8/', page8, name='page8'),
    path('pages/page9/', page9, name='page9'),
    path('pages/page10/', page10, name='page10'),
    path('pages/page11/', page11, name='page11'),
    path('pages/page11/', page11, name='page11'),
    path('pages/page12/', page12, name='page12'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()