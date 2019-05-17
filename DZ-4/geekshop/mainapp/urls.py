from django.conf.urls import url

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    url('^$', mainapp.catalogue, name='index'),
    url(r'^(?P<pk>\d+)/', mainapp.catalogue, name='catalogue'),
    url(r'^product/(?P<pk>\d+)/$', mainapp.product, name='product'),
]
