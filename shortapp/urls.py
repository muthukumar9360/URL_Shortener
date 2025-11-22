from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view/',views.list,name='view'),
    path('<str:short_code>/', views.redirect_short_url, name='redirect'),
]
