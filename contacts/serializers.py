from rest_framework import serializers

from contacts.models import (
    PhoneBook,
    Contact,
    ContactEmail,
    ContactNumber,
    ContactGroup,
    CallLog
)


class ContactEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactEmail
        fields = [
            "email"
        ]


class ContactNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactNumber
        fields = [
            "number",
            "contact_type",
        ]


class ContactSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contact
        fields = [
            "first_name",
            "last_name",
            "favourite",
            "emails",
            "numbers",
            "phonebook"
        ]

    emails = ContactEmailSerializer(many=True, read_only=False)
    numbers = ContactNumberSerializer(many=True, read_only=True)

    def create(self, validated_data):
        emails = validated_data.pop("emails", [])
        numbers = validated_data.pop("numbers", [])
        contact = Contact.objects.create(**validated_data)
        contact_numbers = [
            ContactNumber.objects.create(**number) for number in numbers]
        email_objs = [
            ContactEmail.objects.create(**email) for email in emails
        ]
        contact.emails.add(*email_objs)
        contact.contact_numbers.add(*contact_numbers)
        contact.save()
        return contact


class ContactGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactGroup
        fields = [
            "name",
        ]


class CallLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallLog
        fields = [
            "contact",
            "duration"
        ]


class PhoneBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneBook
        fields = ["title", "user", "owner"]

    owner = serializers.ReadOnlyField(source='user.username')
