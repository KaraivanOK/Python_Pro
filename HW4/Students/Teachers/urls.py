from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_teachers_list,
         name='render_teachers_list'),
]
