"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
import mainapp.views as mainapp
import authapp.views as authapp
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    url(r'^$', mainapp.main, name='main'),
    url(r'^catalogue/', include('mainapp.urls', namespace='catalogue')),
    url(r'^contacts/', mainapp.contacts, name='contacts'),
    url(r'^admin/', include('adminapp.urls', namespace='admin')),
    url(r'^auth/', include('authapp.urls', namespace='auth')),
    url(r'^basket/', include('basketapp.urls', namespace='basket')),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^auth/verify/', include("social_django.urls", namespace="social")),
    url(r'^order/', include('ordersapp.urls', namespace='order')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
