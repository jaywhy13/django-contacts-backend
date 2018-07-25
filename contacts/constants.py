CONTACT_HOME = "home"
CONTACT_WORK = "work"
CONTACT_MOBILE = "mobile"

class ContactType(object):

    CHOICES = (
        (CONTACT_HOME, "Home"),
        (CONTACT_WORK, "Work"),
        (CONTACT_MOBILE, "Mobile")
    )