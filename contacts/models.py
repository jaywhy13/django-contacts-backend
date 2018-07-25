from django.db import models
from django.conf import settings

from django_extensions.db.models import TimeStampedModel


from .constants import ContactType


class PhoneBook(TimeStampedModel):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(TimeStampedModel):

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    emails = models.ManyToManyField("ContactEmail", blank=True)
    contact_numbers = models.ManyToManyField("ContactNumber", blank=True)
    favourite = models.BooleanField(default=False)
    phonebook = models.ForeignKey(PhoneBook, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class ContactEmail(TimeStampedModel):

    email = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email


class ContactNumber(TimeStampedModel):

    number = models.CharField(max_length=11, blank=True, null=True)
    contact_type = models.CharField(max_length=10, choices=ContactType.CHOICES)

    def __str__(self):
        return self.number


class ContactGroup(TimeStampedModel):

    name = models.CharField(max_length=255)
    contacts = models.ManyToManyField(Contact, blank=True)

    def __str__(self):
        return self.name


class CallLog(TimeStampedModel):

    contact = models.ForeignKey("Contact", on_delete=models.CASCADE)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return "Call Log for {}".format(self.contact)
