class Customer:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def customer_given_name(self): 
        print(self.fname)  

    def customer_family_name(self):
        print(self.lname)    

    def customer_full_name(self):
        print(self.fname + self.lname)

class Restaurant:
    def __init__(self, name):
        self.name = name     

    def restaurant_name(self):
        print(self.name)         


class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def rating(self):
        print(self.rating)            