#------------------------
# DATABASE CREDENTIALS  /
#------------------------

user = '****'
password = '*****'
host = "****.rds.amazonaws.com"
port = 3306
database = '****'

#------------------------------------------------------------------------
# Name of columns, ANY CHANGE WILL CREATE A NEW TABLE IN THE DATABASE   /
#------------------------------------------------------------------------

# Define columns and associate var types
input_dict = {
    'ID': 'INT NOT  NULL AUTO_INCREMENT',
    'key1': 'TEXT',
    'key2': 'TEXT',
    'key3': 'TEXT',
    'key4': 'TEXT',
    'key5': 'DECIMAL(24,2) DEFAULT NULL',
    'PRIMARY KEY': '(ID)'
    }
