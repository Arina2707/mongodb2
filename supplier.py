from mongoengine import *


class Events(EmbeddedDocument):
    name = StringField()
    quantity = IntField()
    prestige = IntField()


class SupplierAddress(EmbeddedDocument):
    country = StringField(required=True)
    city = StringField(required=True)
    street = StringField()
    building = IntField()


class Supplier(Document):
    name = StringField(unique=True, required=True)
    address = EmbeddedDocumentField(SupplierAddress)
    university_member = BooleanField(required=True)
    design_lab = BooleanField()
    social_events = EmbeddedDocumentListField(Events)
    quality_system = ListField()
    contact_with_head = BooleanField()

