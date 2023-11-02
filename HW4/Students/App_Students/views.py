from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker
import random
from django.template import loader
from .models import Student

fake = Faker()


def hello_world(request):
    return HttpResponse("Hello world!")


def generate_student(request):
    student_id = random.randint(1, 100)
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = random.randint(18, 65)
    return HttpResponse(f"{student_id}. {first_name} {last_name}, {age} years")


def generate_students(request):
    count = request.GET.get('count')
    if count is None:
        count = 100
    f = [
        f'{fake.first_name()} {fake.last_name()}, '
        f'{random.randint(18, 65)} years\n' for _ in range(int(count))]
    return render(request, 'generate_students.html',
                  {'context': f})


def render_students_list(request):
    students_list = Student.objects.all().values()
    template = loader.get_template('students_list.html')
    context = {
        'students': students_list,
    }
    return HttpResponse(template.render(context, request))
