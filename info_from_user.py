import datetime


def ask_supplier():
    name = input("Enter the name:")
    country = input("Enter the country:")
    city = input("Enter the city: ")
    street = input("Enter the street:")
    building = int(input("Enter the building:"))
    university = bool(int(input("Is it the university member (0 or 1)?")))
    design_lab = bool(int(input("Is there a design lab (0 or 1)?")))
    contact_dir = bool(int(input("Did you have contact with director (0 or 1)?")))

    input_string1 = input("Enter a list of ISO standards: ")
    quality_system = input_string1.split()
    num = int(input("Enter the number of events you'd like to add to the list:"))
    return name, country, city, street, building, university, design_lab, contact_dir, quality_system, num


def ask_events():
        name = input("Enter the name:")
        quant = int(input("Enter the quantity:"))
        pr = input("Enter the prestige:")
        return name, quant, pr


def ask_delivery_items():
        spec = input("Enter the specification:")
        quant = int(input("Enter the quantity:"))
        un = input("Enter the unit:")
        unp = float(input("Enter the price for unit:"))
        curr = input("Enter the currency:")
        inn_st = bool(int(input("Enter the innovation stage (0 or 1):")))
        ext = int(input("Enter the number of extra profits:"))
        return spec, quant, un, unp, curr, inn_st, ext


def ask_delivery_doc():
    name = input("Enter the name:")
    doc_c = input("Enter the document code:")
    date_entry = input('Enter a date (i.e. 2017,7,1)')
    year, month, day = map(int, date_entry.split(','))
    doc_data = datetime.datetime(year, month, day)

    contact_person = input("Enter the contact person:")
    contact_email = input("Enter the contact email:")
    terms_of_delivery = input("Enter terms of delivery:")
    time_of_delivery = input("Enter time of delivery:")
    terms_of_payment = input("Enter terms of payment:")
    warranty = input("Enter warranty:")
    post_m = input("Enter the number of postponed meetings:")

    des_dec = int(input("Enter the number of unusual design decisions:"))
    cont_t = int(input("Enter the number of contact time days:"))
    or_req = int(input("Enter the number of original requests bout the product:"))
    f_req = int(input("How much of them were realized?"))
    req = {"original": or_req, "total": f_req}

    cont_s = int(input("Enter the realized scopes of supplement change:"))
    def_quant = int(input("Enter the quantity of defected goods:"))
    del_days = int(input("Enter the delivery time days:"))
    del_on_t = bool(int(input("Were items delivered on time (0 or 1)?")))
    deliv = {"scope_of_supplement_change": cont_s, "quantity_defective_goods": def_quant, "delivery_time_days": del_days, "on_time_delivered": del_on_t}

    number = int(input("Enter the number of items you'd like to add to the list:"))
    return name, doc_c, doc_data, contact_person, contact_email, terms_of_delivery, time_of_delivery, terms_of_payment, warranty, des_dec, cont_t, req, deliv, number,post_m


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
    post_m = input("Enter the number of postponed meetings:")
    des_dec = int(input("Enter the number of unusual design decisions:"))
    cont_t = int(input("Enter the number of contact time days:"))
    or_req = int(input("Enter the number of original requests bout the product:"))
    f_req = int(input("How much of them were realized?"))
    req = {"original": or_req, "total": f_req}

    cont_s = int(input("Enter the realized scopes of supplement change:"))
    def_quant = int(input("Enter the quantity of defected goods:"))
    del_days = int(input("Enter the delivery time days:"))
    del_on_t = bool(int(input("Were items delivered on time (0 or 1)?")))
    deliv = {"scope_of_supplement_change": cont_s, "quantity_defective_goods": def_quant, "delivery_time_days": del_days, "on_time_delivered": del_on_t}

    number = int(input("Enter the number of items you'd like to add to the list:"))
    return doc_c, doc_data, contact_person, contact_email, terms_of_delivery, time_of_delivery, terms_of_payment, warranty, des_dec, cont_t, req, deliv, number, post_m