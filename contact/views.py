from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def all_contacts(request):
    return HttpResponse("All Contacts")