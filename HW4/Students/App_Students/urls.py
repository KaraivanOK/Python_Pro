from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello-world'),
    path('generate-student/', views.generate_student, name='generate-student'),
    path('generate-students/', views.generate_students,
         name='generate-students'),
    path('', views.render_students_list,
         name='render-students-list'),
]
