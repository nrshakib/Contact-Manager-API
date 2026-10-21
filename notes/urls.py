from django.urls import path
from rest_framework import routers

from notes import views

router = routers.SimpleRouter()
router.register(r'', views.NotesViewSet)

urlpatterns = router.urls