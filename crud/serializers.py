from rest_framework import serializers
from .models import Student, Group, Curator, Faculty


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CuratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curator
        fields = '__all__'


class FacultySerializer(serializers.HyperlinkedModelSerializer):
    group = GroupSerializer(many=True)

    class Meta:
        model = Faculty
        fields = '__all__'
