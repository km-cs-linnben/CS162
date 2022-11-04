"""

CS161
Week 9
Wednesday
1) Assignment 9
"""

class Cat:

    # class attributes
    species = "feline"

    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age


class DomesticCat(Cat):
    """Cats that are pets."""


my_cat = Cat("American shorthair", "Baby", 9)
# print(f"\nI have a {my_cat.age} years old {my_cat.breed} whose name is {my_cat.name}.")

# print(f"\nClass attribute: {Cat.species}.")
# print(f"\nMy cat's class attribute is {my_cat.species}.")

# your_cat = Cat("Birman", "Kitty", 5)
# print(f"\nYou have a {your_cat.age} years old {your_cat.breed} whose name is {your_cat.name}.")
# print(f"\nYour cat's class attribute is {my_cat.species}.")

# What does isinstance() do? How do we use it?
#print(isinstance(my_cat, Cat))

their_cat = DomesticCat("Russian blue", "Alienware", 1)
# print(isinstance(their_cat, (DomesticCat)))
# print(isinstance(their_cat, Cat))


class KenShoppingCart:
    """A shopping cart."""

    def __init__(self, items, coupons):

        self.items = list(items)
        self.coupons = list(coupons)


class MattShoppingCart:

    def __init__(self, capacity, rating, price):
        self.capacity = capacity
        self.rating = rating
        self.price = price

    def cart():  # functions, use verb()
        """If a store is going to buy the product?"""
        capacity = input("What is the capacity? (small, medium, large) -> ")
        print(capacity)
        rating = input("What is the rating? Up to 5 stars -> ")
        print(str(rating))
        price = input("Enter the price: -> ")
        print(str(price))

# ShoppingCart.cart()


class ShoppingCart:
    """Add/store/delete/check products; show the customer's name."""

    def __init__(self, name):
        self.name = name  # customer name
        self.items = []  # empty list which will hold the customer's products

    def add_item(self, *products):  # *args, unlimited positional arguments
        """
        Add items to the card.
        Args: *items: tuple
        """
        for i in products:
            self.items.append(i)

    def remove_item(self, *products):
        """
        Add items to the card.
        Args: *items: tuple
        """
        for i in products:
            if i in self.items:
                self.items.remove(i)
                print(f"\n{i} is now removed.\n")
            else:
                print(f"\nThis item: {i}, is not in your cart.\n")
        return self.items

    def __str__(self):
        return f"{self.name}'s shopping cart has: {self.items}."


# my_cart = ShoppingCart("Anais")

# my_cart.add_item("Cat bed", "Mugs", "iPhone")
# print(my_cart) # Anais's shopping cart has: ['Cat bed', 'Mugs', 'iPhone'].
# print("\nAnais wants to remove something from the cart.")

# print(my_cart.remove_item("Cat food", "iPhone"))

class PrestonShoppingCart:
    def __init__(self):
        self.cart_inventory = {}

    def add_to_cart(self, item, amount):
        if item not in self.cart_inventory:
            self.cart_inventory[item] = amount
        else:
            self.cart_inventory[item] += amount
        return self.cart_inventory
    
    def remove_from_cart(self, item, amount):
        """Remove items from the cart."""
        # Suggestion 1
        # try:
        #     self.cart_inventory[item] -= amount
        # except:
        #     print (f"Item ({item}) is not in the cart.")
        # return self.cart_inventory

        # Suggestion 2
        # if not self.cart_inventory.get(item):
        #     print(f"{item} is not in the cart.")
        # else:
        #     self.cart_inventory[item] -= amount
        # return self.cart_inventory
    
    def update_cart(self, item, amount):
        self.cart_inventory[item] = amount
        return self.cart_inventory

my_cart = PrestonShoppingCart()
print("\nAdd 1 Stereo to the cart.")
my_cart.add_to_cart("Stereo", 1)

print(my_cart.cart_inventory)

print("\nAdd 20 Milk to the cart.")
my_cart.add_to_cart("Milk", 20)
print(my_cart.cart_inventory)

print("\n Remove something from the cart.")
my_cart.remove_from_cart("Milk", 3) # Milk: 17
print(my_cart.cart_inventory)

# print("\nAdd 1 more Milk to the cart.")
# my_cart.add_to_cart("Milk", 1)
# print(my_cart.cart_inventory)

# print("\nUpdate Stereo amount to 5.")
# my_cart.update_cart("Stereo", 5)
# print(my_cart.cart_inventory)

# print("\n Decrement Milk by 2.")
# my_cart.add_to_cart("Milk", -2) 
# print(my_cart.cart_inventory)