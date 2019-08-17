from rest_framework import serializers
from .models import Student, Group, Curator, Faculty, Diploma, Ball, Work


class CuratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curator
        fields = ('id', 'name', 'surname', 'description', 'photo')


class BallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ball
        fields = ('id', 'math', 'physical', 'programing')


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Work
        fields = ('id', 'title', 'city')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    curator = CuratorSerializer()

    class Meta:
        model = Group
        fields = '__all__'


class DiplomaSerializer(serializers.HyperlinkedModelSerializer):
    curator = CuratorSerializer()

    class Meta:
        model = Diploma
        fields = ('id', 'title', 'curator')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    ball = BallSerializer()
    diploma = DiplomaSerializer()
    group = GroupSerializer()
    work = WorkSerializer()
    curator = CuratorSerializer()

    class Meta:
        model = Student
        fields = ('id', 'name', 'surname', 'patronymic', 'photo', 'group', 'ball',
                  'diploma', 'work', 'curator', 'year_end', 'description')


class FacultySerializer(serializers.HyperlinkedModelSerializer):
    group = GroupSerializer(many=True)

    class Meta:
        model = Faculty
        fields = ('id', 'name', 'group')



