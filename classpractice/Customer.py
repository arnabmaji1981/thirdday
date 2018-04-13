class Customer:
    def __init__(self,r, s):
        self.name = r
        self.shipping_address = s
    def search_product(self,product_name):
        print(product_name)
    def browse_product(self,product_name):
        print("browsing "+ product_name)

cust1 = Customer("abdul", "bangalore")
cust1.search_product("phone")
print(cust1.name)
print("") # to insert black space
cust2 = Customer("juwes", "shillong")
cust2.search_product("mobile")
print(cust2.name)

