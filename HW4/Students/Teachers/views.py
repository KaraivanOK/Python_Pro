from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Teacher


def render_teachers_list(request):
    teachers_list = Teacher.objects.all().values()
    template = loader.get_template('teachers_list.html')
    context = {
        'teachers': teachers_list,
    }
    return HttpResponse(template.render(context, request))
