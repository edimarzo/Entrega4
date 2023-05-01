from django.urls import path
from inicio import views

app_name='inicio'

urlpatterns = [
    path('', views.inicio,name= 'inicio'),
    path('sobre-mi', views.sobre_mi,name= 'sobre_mi'),
    # path('alta-producto', views.AltaCategoria.as_view(), name='altacat'),
    path('alta-producto', views.AltaProducto.as_view(), name='altaprod'),
    path('lista-producto', views.ListaProducto.as_view(), name='listaprod2'),
    path('alta-persona', views.AltaPersona.as_view(), name='altapers'),
    path('persona', views.BusquedaPersona.as_view(), name='listapersona'),
    path('persona/<int:pk>/eliminar/', views.PersonaDeleteView.as_view(), name='bajapersona'),
    path('persona/<int:pk>/modificar/', views.PersonaUpdateView.as_view(), name='modpersona'),
    path('producto', views.SearchResultsListView.as_view(), name='listaprod'),
    path('producto/<int:pk>/modificar/', views.ProductoUpdateView.as_view(), name='modprod'),
    path('producto/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='bajaprod'),
    

    
    
]