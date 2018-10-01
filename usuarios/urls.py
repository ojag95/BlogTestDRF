from django.conf.urls import url
from usuarios import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^usuarios/$', views.lista_usuarios),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.detalle_usuarios),
]

urlpatterns = format_suffix_patterns(urlpatterns)