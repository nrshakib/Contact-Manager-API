from django.urls import path

from contact import views


urlpatterns = [
    path('contacts/', views.all_contacts, name = "all contacts")
]