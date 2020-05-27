from supplier import *
from delivery import *
from info_from_user_light import *
import pymongo
from bson.objectid import ObjectId
import datetime


def add_supplier_doc_light():

    name, country, city, street, build, univ = ask_supplier()
    supplier = Supplier()
    supplier.name = name
    supplier.address = SupplierAddress()
    supplier.address.country = country
    supplier.address.city = city
    supplier.address.street = street
    supplier.address.building = build
    supplier.university_member = univ

    supplier.save()

    dc, dd, cn, em, teod, tiod, teop, warr, num = ask_delivery_doc_supplier()
    delivery = Delivery()
    delivery.name = supplier.id
    delivery.doc_code = dc
    delivery.contact = ContactDelivery(contact_name=cn, email=em)
    delivery.delivery_rules = DeliveryRules(terms_of_delivery=teod, time_of_delivery=tiod, terms_of_payment=teop,
                                            warranty=warr)
    delivery.doc_date = dd
    delivery.items = []
    for i in range(0, num):
        spec, quant, un, unp, curr = ask_delivery_items()
        delivery.items.append(Items(specification=spec, quantity=quant, unit=un, unit_price=unp, currency=curr))

    delivery.save()


def add_supplier_light():
    name, country, city, street, build, univ = ask_supplier()
    supplier = Supplier()
    supplier.name = name
    supplier.address = SupplierAddress()
    supplier.address.country = country
    supplier.address.city = city
    supplier.address.street = street
    supplier.address.building = build
    supplier.university_member = univ

    supplier.save()


def add_doc_light(mycoll):
    dc, name, dd, cn, em, teod, tiod, teop, warr, num = ask_delivery_doc()

    z = mycoll.find({'name': {'$eq': name}}, {"_id": 1})
    original_id = ObjectId()
    for elem in z:
        original_id = elem['_id']
        print(type(original_id))

    delivery = Delivery()
    delivery.name = original_id
    delivery.doc_code = dc
    delivery.contact = ContactDelivery(contact_name=cn, email=em)
    delivery.delivery_rules = DeliveryRules(terms_of_delivery=teod, time_of_delivery=tiod, terms_of_payment=teop,
                                            warranty=warr)
    delivery.doc_date = dd
    delivery.items = []
    for i in range(0, num):
        spec, quant, un, unp, curr = ask_delivery_items()
        delivery.items.append(Items(specification=spec, quantity=quant, unit=un, unit_price=unp, currency=curr))

    delivery.save()
