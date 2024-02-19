class Product():
    code:int
    name:str
    supplier:str
    price:int
    def info(self):
        print(" product code ",self.code,"name ",self.name)
prod1 = Product()
prod1.code =1
prod1.name="Laptop"
prod1.supplier="HP"
prod1.price = 65000
prod1.info()

print("constructor")
class Customer():
    #constructor
    def __init__(self,code,name,email,mobile):
        self.code = code
        self.name = name
        self.email = email
        self.mobile = mobile
    def __str__(self):
        return "testing str  "

    def info(self):
        print("code ",self.code,"name ",self.name)

cust1 = Customer(1,"ravi","ravi@gmail.com",9845547471)
print(cust1)
print(cust1.info())











