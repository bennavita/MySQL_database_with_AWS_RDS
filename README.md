General module in order to interact with a relational database from Amazon Webservices.
The current set up is made for MySQL and uses port 3306 but can easily be adapted for others.
It might be the objective of one future commit.

-> The main feature is to provide the Database with data using a DataFrame.
It is advised to create your DataFrame using the input_dict.

Prior to use :
Create AWS RDS Database instance in MYSQL and set the security rules to All kind of traffic.

# manage_database.ipynb
There is a jupyter notebook (manage_database.ipynb) that allows to implement some tests while setting up some tables.
Create, verify and delete some tables with more flexibility.

# manage_database.py
This file is built in order to interact with a project.
It is dynamic and the structure of the table, name of the database, name of the table are filled in the credentials.py file.

# Credentials
This is where you will apply your database credentials and modify columns and variable types according to your needs.