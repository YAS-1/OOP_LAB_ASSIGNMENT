class Customer:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def display_info(self):
        return f'Customer name: {self.name}, Customer address: {self.address}'

if __name__=='__main__':
    customer1 = Customer('Arthur','Kampala')

    print(customer1.display_info())