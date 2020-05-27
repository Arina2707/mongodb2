from supplier import *
from delivery import *
from info_from_user import *
import pymongo
from bson.objectid import ObjectId
import datetime


def add_supplier_doc():

    name, country, city, street, build, univ, design_l, contact_d, quality_s, num = ask_supplier()
    supplier = Supplier()
    supplier.name = name
    supplier.address = SupplierAddress()
    supplier.address.country = country
    supplier.address.city = city
    supplier.address.street = street
    supplier.address.building = build
    supplier.university_member = univ
    supplier.design_lab = design_l
    supplier.contact_with_head = contact_d
    supplier.quality_system = quality_s

    supplier.social_events = []
    for i in range(0, num):
        n, q, p = ask_events()
        supplier.social_events.append(Events(name=n, quantity=q, prestige=p))

    supplier.save()

    dc, dd, cn, em, teod, tiod, teop, warr, des_dec, cont_t, req, deliv, num, pp = ask_delivery_doc_supplier()
    delivery = Delivery()
    delivery.name = supplier.id
    delivery.doc_code = dc
    delivery.contact = ContactDelivery(contact_name=cn, email=em)
    delivery.delivery_rules = DeliveryRules(terms_of_delivery=teod, time_of_delivery=tiod, terms_of_payment=teop,
                                            warranty=warr)

    delivery.design_decision = des_dec
    delivery.original_final_ratio = req
    delivery.delivery_indicators = deliv
    delivery.contact_time_days = cont_t
    delivery.doc_date = dd
    delivery.postponed_meetings = pp

    delivery.items = []
    for i in range(0, num):
        spec, quant, un, unp, curr, inn_st, ext = ask_delivery_items()
        delivery.items.append(Items(specification=spec, quantity=quant, unit=un, unit_price=unp, currency=curr, innovation_stage=inn_st, extras=ext))

    delivery.save()


def add_supplier():
    name, country, city, street, build, univ, design_l, contact_d, quality_s, num = ask_supplier()

    supplier = Supplier()
    supplier.name = name
    supplier.address = SupplierAddress()
    supplier.address.country = country
    supplier.address.city = city
    supplier.address.street = street
    supplier.address.building = build
    supplier.university_member = univ
    supplier.design_lab = design_l
    supplier.contact_with_head = contact_d
    supplier.quality_system = quality_s

    supplier.social_events = []
    for i in range(0, num):
        n, q, p = ask_events()
        supplier.social_events.append(Events(name=n, quantity=q, prestige=p))

    supplier.save()


def add_doc(mycoll):
    name, dc, dd, cn, em, teod, tiod, teop, warr, des_dec, cont_t, req, deliv, num, pp = ask_delivery_doc()

    z = mycoll.find({'name': {'$eq': name}}, {"_id": 1})
    original_id = ObjectId()
    for elem in z:
        original_id = elem['_id']

    delivery = Delivery()
    delivery.name = original_id
    delivery.doc_code = dc
    delivery.contact = ContactDelivery(contact_name=cn, email=em)
    delivery.delivery_rules = DeliveryRules(terms_of_delivery=teod, time_of_delivery=tiod, terms_of_payment=teop,
                                            warranty=warr)
    delivery.design_decision = des_dec
    delivery.original_final_ratio = req
    delivery.delivery_indicators = deliv
    delivery.contact_time_days = cont_t
    delivery.doc_date = dd
    delivery.postponed_meetings = pp
    delivery.items = []
    for i in range(0, num):
        spec, quant, un, unp, curr, inn_st, ext = ask_delivery_items()
        delivery.items.append(Items(specification=spec, quantity=quant, unit=un, unit_price=unp, currency=curr, innovation_stage=inn_st, extras=ext))

    delivery.save()
