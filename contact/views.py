from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from contact.models import Contact
from contact.serializer import ContactSerializer

from utils.utils import api_response

# Create your views here.
# generic api view with mixin
class ContactListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)

        return api_response(
            message="All Contacts retrieved successfully",
            data=response.data,
            status_code=response.status_code
            )
    

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)

        return api_response(
            message="Contact created successfully",
            data=response.data,
            status_code=response.status_code,
        )

class ContactRetrieveUpdateDeleteView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'id'
    
    def get(self, request, *args, **kwargs):
        response = self.retrieve(request, *args, **kwargs)
        
        return api_response(
            message="Contact retrieved successfully",
            data=response.data,
            status_code=response.status_code,
        )
    

    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)

        return api_response(
            message="Contact updated successfully",
            data=response.data,
            status_code=response.status_code,
        )

    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)

        return api_response(
            message="Contact partially updated successfully",
            data=response.data,
            status_code=response.status_code,
        )
    
    def delete(self, request, *args, **kwargs):
        self.get_object()
        self.perform_destroy(self.get_object())

        return api_response(
            message="Contact deleted successfully",
            data=None,
            status_code=response.status_code,
        )
