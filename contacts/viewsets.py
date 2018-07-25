from rest_framework import viewsets

from contacts.models import (
    PhoneBook,
    Contact,
    ContactEmail,
    ContactNumber,
    ContactGroup,
    CallLog
)
from .serializers import (
    PhoneBookSerializer,
    ContactSerializer,
    ContactGroupSerializer,
    ContactNumberSerializer,
    ContactEmailSerializer,
)


class PhoneBookViewSet(viewsets.ModelViewSet):

    queryset = PhoneBook.objects.all()
    serializer_class = PhoneBookSerializer


class ContactViewSet(viewsets.ModelViewSet):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactGroupViewSet(viewsets.ModelViewSet):

    queryset = ContactGroup.objects.all()
    serializer_class = ContactGroupSerializer


class ContactEmailViewSet(viewsets.ModelViewSet):

    queryset = ContactEmail.objects.all()
    serializer_class = ContactEmailSerializer


class ContactNumberViewSet(viewsets.ModelViewSet):

    queryset = ContactNumber.objects.all()
    serializer_class = ContactNumberSerializer
