class Customer:
    __CUSTOMER_LIST = []

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    @classmethod
    def add_customer(cls, name, email):
        # Use a dictionary to store customer data
        cls.__CUSTOMER_LIST.append({"name": name, "email": email})

    @classmethod
    def getCustomer(cls):
        # Return the customer list
        return cls.__CUSTOMER_LIST
