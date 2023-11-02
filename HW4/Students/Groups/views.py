from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Group


def render_groups_list(request):
    groups_list = Group.objects.all().values()
    template = loader.get_template('groups_list.html')
    context = {
        'groups': groups_list,
    }
    return HttpResponse(template.render(context, request))
