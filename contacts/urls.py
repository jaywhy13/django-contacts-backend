from rest_framework import routers

from .viewsets import (
    PhoneBookViewSet,
    ContactViewSet,
    ContactEmailViewSet,

)

router = routers.DefaultRouter()
router.register('phonebook', PhoneBookViewSet)
router.register('contact', ContactViewSet)
router.register('email', ContactEmailViewSet)
