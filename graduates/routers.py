from rest_framework import routers
from crud.viewsets import StudentViewSet


router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
