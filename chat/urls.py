from django.urls import path
from chat import views

app_name='chat'

urlpatterns = [
    path('chat/', views.chatPage, name="chat-page")]
