from django.db import models

from django_extensions.db.models import TimestampedModel


from .constants import ContactType


class Contact(TimestampedModel):

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    emails = models.ManyToManyField("Email", blank=True)
    contact_numbers = models.ManyToManyField("ContactNumber", blank=True)
    favourite = models.BooleanField(default=False)


class Email(TimestampedModel):

    email = models.CharField(max_length=255, blank=True, null=True)


class ContactNumber(TimestampedModel):

    number = models.CharField(max_length=11, blank=True, null=True)
    contact_type = models.CharField(max_length=10, choices=ContactType.CHOICES)


class ContactGroup(TimestampedModel):

    name = models.CharField(max_length=255)
    contacts = models.ManyToManyField(blank=True)


class CallLog(TimestampedModel):

    contact = models.ForeignKey("Contact")
    duration = models.IntegerField(default=0)
