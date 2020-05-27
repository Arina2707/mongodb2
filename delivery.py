from mongoengine import *
from supplier import *
import datetime


class ContactDelivery(EmbeddedDocument):
    contact_name = StringField()
    email = EmailField()


class DeliveryRules(EmbeddedDocument):
    terms_of_delivery = StringField()
    time_of_delivery = StringField()
    terms_of_payment = StringField()
    warranty = StringField()


class Items(EmbeddedDocument):
    specification = StringField(required=True)
    quantity = IntField(required=True)
    unit = StringField(required=True)
    unit_price = FloatField(required=True)
    currency = StringField(required=True)
    innovation_stage = BooleanField()
    extras = IntField()


class Delivery(Document):
    doc_code = StringField(unique=True, required=True)
    name = ReferenceField('Supplier', dbref=False, reverse_delete_rule=0, required=True)
    contact = EmbeddedDocumentField(ContactDelivery)
    delivery_rules = EmbeddedDocumentField(DeliveryRules)
    items = EmbeddedDocumentListField(Items)
    registered_date = DateTimeField(default=datetime.datetime.now, required=True)
    doc_date = DateTimeField(required=True)
    design_decision = IntField()
    original_final_ratio = DictField()
    delivery_indicators = DictField()
    contact_time_days = IntField()
    postponed_meetings = IntField()
