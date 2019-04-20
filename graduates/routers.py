from rest_framework import routers
from crud.viewsets import StudentViewSet, GroupViewSet, CuratorViewSet, FacultyViewSet


router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'curators', CuratorViewSet)
router.register(r'faculty', FacultyViewSet)
