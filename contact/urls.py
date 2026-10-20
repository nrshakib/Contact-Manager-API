from django.urls import path

from contact import views


urlpatterns = [
    path(
        'contacts/',
         views.ContactListCreateView.as_view(),
         name = "all-contacts"),

    # path(
    #     'contacts/<int:id>/',
    #      views.ContactRetrieveUpdateDeleteView.as_view(),
    #      name = "single-contact"),
]