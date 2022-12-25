# Database credentials

user = '****'
password = '****!'
host = "****.rds.amazonaws.com"
port = 3306
database = '****'

# Define columns and associate var types
# ANY CHANGE WILL CREATE A NEW TABLE IN THE DATABASE
input_dict = {
    'ID': 'INT NOT  NULL AUTO_INCREMENT',
    'key1': 'TEXT',
    'key2': 'TEXT',
    'key3': 'TEXT',
    'key4': 'TEXT',
    'key5': 'DECIMAL(24,2) DEFAULT NULL',
    'PRIMARY KEY': '(ID)'
    }
