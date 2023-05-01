from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('perfil/editar', views.editar_perfil,name='editar'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
]
