from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response

from contact.models import Contact
from contact.serializer import ContactSerializer

# Create your views here.
# generic api view with mixin
class ContactListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)

        return Response({
            "message": "Contacts retrieved successfully",
            "data": response.data
            },
            status=response.status_code)
    

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)

        return Response({
            "message": "Contact created successfully",
            "data": response.data
            },
            status=response.status_code)
