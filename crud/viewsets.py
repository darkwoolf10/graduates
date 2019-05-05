from rest_framework import viewsets
from .models import Student, Group, Curator, Faculty, Diploma, Ball, Work
from .serializers import StudentSerializer, GroupSerializer, CuratorSerializer, \
    FacultySerializer, DiplomaSerializer, BallSerializer, WorkSerializer


class BallViewSet(viewsets.ModelViewSet):
    queryset = Ball.objects.all()
    serializer_class = BallSerializer


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class CuratorViewSet(viewsets.ModelViewSet):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer


class DiplomaViewSet(viewsets.ModelViewSet):
    queryset = Diploma.objects.all()
    serializer_class = DiplomaSerializer
