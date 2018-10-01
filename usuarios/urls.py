from django.conf.urls import url
from usuarios import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^usuarios/$', views.ListadoUsuarios.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UsuarioDetalles.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)