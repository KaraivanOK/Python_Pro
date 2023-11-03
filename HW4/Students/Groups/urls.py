from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_groups_list,
         name='render_groups_list'),
]
