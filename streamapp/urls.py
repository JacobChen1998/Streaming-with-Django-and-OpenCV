from django.urls import path, include
from streamapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('webstramfunc', views.webstramfunc, name='webstramfunc'),
    ]
