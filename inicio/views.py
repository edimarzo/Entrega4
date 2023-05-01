
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from inicio import models

def inicio(request):
    return render(request,'inicio.html')

def sobre_mi(request):
    return render(request, 'sobre_mi.html')


class SearchResultsListView(FilterView):
    model = models.Producto
    context_object_name = 'lista'
    filterset_fields = ['item']
    template_name = 'lista_productosv2.html'


class AltaProducto(CreateView):
    model = models.Producto
    template_name = "alta_producto.html"
    fields = ['item','descripcion','cantidad']
    success_url = '/alta-producto'
    
class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Producto
    template_name = "baja_producto.html"
    success_url = '/producto'
    
class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Producto
    template_name = "modificar_producto.html"
    success_url = '/producto'
    fields = ['descripcion', 'cantidad']
    
class ListaProducto(ListView):
    model = models.Producto
    template_name = "lista_productos.html"

class AltaPersona(CreateView):
    model = models.Persona
    template_name = "alta_persona.html"
    fields = ['nombre','apellido','legajo','fecha_nacimiento']
    success_url = '/alta-persona'

class BusquedaPersona(FilterView):
    model = models.Persona
    context_object_name = 'lista'
    filterset_fields = ['apellido']
    template_name = 'lista_persona.html'

class PersonaDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Persona
    template_name = "baja_persona.html"
    success_url = '/persona'

class PersonaUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Persona
    template_name = "modificar_persona.html"
    success_url = '/persona'
    fields = ['nombre', 'apellido']