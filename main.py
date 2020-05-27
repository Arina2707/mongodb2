from connection import cluster_connection
from data_service import add_supplier_doc, add_supplier, add_doc
from data_service_light import add_supplier_doc_light, add_supplier_light, add_doc_light


def main():
    print("Let's start!")

    mycoll = cluster_connection()

    str_input = int(input("1 - add supplier, 2 - add only document, 3 - add supplier and his document,\n4 - add supplier light, 5 - add only document light, 6 - add supplier and his document light"))
    if str_input == 1:
        add_supplier()
    elif str_input == 2:
        add_doc(mycoll)
    elif str_input == 3:
        add_supplier_doc()
    elif str_input == 4:
        add_supplier_light()
    elif str_input == 5:
        add_doc_light()
    elif str_input == 6:
        add_supplier_doc_light()


if __name__ == '__main__':
    main()
