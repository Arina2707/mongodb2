# Laser supplier info collection and aggregation 

This is the first part of the project, connected with laser suppliers (the second one - )
That project provides tool for data collection about the laser suppliers for the company.
The information flow consists of 3 main stages: information collection and storaging in in MongoDB Atlas. 
Also, working with MongoDB, such as writing, reading, quering.

The overall schema of info collection and aggregation is shown in Pic.1.

![Pic.1](https://user-images.githubusercontent.com/56595596/144017661-653a4d20-76b4-47a4-b415-aff71ca995ee.png)

## Scripts description
main – main classes and methods are called from it.

connection – this file contains the class through which the connection to the database is made.

supplier – a file containing the Supplier class and it's nested SupplierAddress class (MongoEngine – Document-Object Mapper used).

delivery – it contains the main class Delivery, and childs: ContactDelivery, DeliveryRules, Items (MongoEngine – Document-Object Mapper used).

data_service – a pro file with functions that cause writing to our classes (add_doc, add_supplier, add_supplier_doc).

info_from_users – a pro file with functions that interacts with users.

data_service_light – a simplified file with functions that cause writing to our classes (add_doc, add_supplier, add_supplier_doc).

info_from_users_light – a simplified function file that interacts with users.



