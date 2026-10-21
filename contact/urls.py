from django.urls import path

from contact import views


urlpatterns = [
    path(
        'all/',
         views.ContactListCreateView.as_view(),
         name = "all-contacts"),

    path(
        'contact/<int:id>/',
         views.ContactRetrieveUpdateDeleteView.as_view(),
         name = "single-contact"),
]