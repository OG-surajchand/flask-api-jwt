#DB CREDENTIALS
MONGO_URI = 'mongodb://localhost:27017/Customer'
DATABASE = 'Customer'
CUSTOMER_COLLECTION = 'customer_detail'

USER_LIST = [
    {"username": "Admin", "password": "Admin123", "roles": "admin"},
    {"username": "readUser", "password": "Admin123", "roles": "read"},
    {"username": "writeUser", "password": "Admin123", "roles": "write"}
]
WRITE_ROLES = ['admin', 'write']