from django.conf.urls import url
from usuarios import views

urlpatterns = [
    url(r'^usuarios/$', views.lista_usuarios),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.detalle_usuarios),
]