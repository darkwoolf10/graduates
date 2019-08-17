from django.shortcuts import render
from .models import Student, Curator
from .forms import CuratorsForm
from django.core import serializers
from django.http import JsonResponse, HttpResponseRedirect


# Create your views here.


def index(request):
    return render(request, 'index.html')


def curators(request):
    curators = Curator.objects.all()
    return render(request, 'curators.html', {'curators': curators})


def create_curator(request):
    if request.method == 'POST':
        form = CuratorsForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/crud/')
    else:
        form = CuratorsForm()

    return render(request, 'create-curator.html', {'form': form})


def statistic(request):
    students = Student.objects.raw('SELECT * from crud_student ORDER BY crud_student.name ASC')
    graduates = Student.objects.raw('''
        SELECT * from crud_student INNER JOIN crud_ball ON crud_ball.id = crud_student.ball_id 
        WHERE (math + physical + programing) / 3 >= 90
    ''')
    sovietStudent = Student.objects.raw('SELECT * from crud_student WHERE crud_student.year_end < 1991')
    groupStudent = Student.objects.raw('''
        SELECT * FROM crud_student INNER JOIN crud_group ON crud_group.id = crud_student.group_id
        WHERE crud_group.name = 'КС-16'
    ''')

    return render(request, 'statistic.html', {
        'students': students,
        'graduates': graduates,
        'sovietStudent': sovietStudent,
        'groupStudent': groupStudent,
    })


def show_excellent_pupil(request):
    students = Student.objects.raw('SELECT * from crud_student')
    students_serialized = serializers.serialize('json', students)
    return JsonResponse(students_serialized, safe=False)


def show_good_students(request):
    return
