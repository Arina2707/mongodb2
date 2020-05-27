import datetime


def ask_supplier():
    name = input("Enter the name:")
    country = input("Enter the country:")
    city = input("Enter the city: ")
    street = input("Enter the street:")
    building = int(input("Enter the building:"))
    university = bool(int(input("Is it the university member (0 or 1)?")))
    return name, country, city, street, building, university


def ask_delivery_items():
        spec = input("Enter the specification:")
        quant = int(input("Enter the quantity:"))
        un = input("Enter the unit:")
        unp = float(input("Enter the price for unit:"))
        curr = input("Enter the currency:")
        return spec, quant, un, unp, curr


def ask_delivery_doc():
    doc_c = input("Enter the document code:")
    date_entry = input('Enter a date (i.e. 2017,7,1)')
    year, month, day = map(int, date_entry.split(','))
    doc_data = datetime.datetime(year, month, day)

    name = input("Enter the name:")
    contact_person = input("Enter the contact person:")
    contact_email = input("Enter the contact email:")
    terms_of_delivery = input("Enter terms of delivery:")
    time_of_delivery = input("Enter time of delivery:")
    terms_of_payment = input("Enter terms of payment:")
    warranty = input("Enter warranty:")
    number = int(input("Enter the number of items you'd like to add to the list:"))
    return doc_c, name, doc_data, contact_person, contact_email, terms_of_delivery, time_of_delivery, terms_of_payment, warranty, number


def ask_delivery_doc_supplier():
    doc_c = input("Enter the document code:")
    date_entry = input('Enter a date (i.e. 2017,7,1)')
    year, month, day = map(int, date_entry.split(','))
    doc_data = datetime.datetime(year, month, day)

    contact_person = input("Enter the contact person:")
    contact_email = input("Enter the contact email:")
    terms_of_delivery = input("Enter terms of delivery:")
    time_of_delivery = input("Enter tme of delivery:")
    terms_of_payment = input("Enter terms of payment:")
    warranty = input("Enter warranty:")
    number = int(input("Enter the number of items you'd like to add to the list:"))
    return doc_c, doc_data, contact_person, contact_email, terms_of_delivery, time_of_delivery, terms_of_payment, warranty, number