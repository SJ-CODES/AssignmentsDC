# class Store: 
#   def __init__(self, name, address): 
#     self.name = name 
#     self.address = address 

# print("Enter 1 to add a store: ")
# print("Enter 2 to add item to a store: ")
# print("Enter q to quit: ")

# while True: 
#   choice = input("Enter choice: ")
  
#   if choice == "1":
#     store_name = input("Enter store name: ")
#     store_address = input("Enter store address: ")
#     store = Store(store_name, store_address)
#     stores.append(store)
  
#   elif choice == "2": 
#     # display all stores 
#     1. HEB 
#     2. Fiesta 
#     3. Walmart 
#     # ask the user which store they want to add the item 
#     input("Whuch store you want to add ") 
#     1 
#     store = stores[1-1]
#     item = Item("Milk", 5.60, 2)
#     store.items.append(item)









grocery_stores = []
print(grocery_stores)

class Grocery_store:
    def __init__(self,store_name,store_address):
        self.store_name = store_name
        self.store_address = store_address
class Items:
    def _init_ (self, item_name , price, quantity):
         self.item_name = item_name
         self.price = price
         self.quantity = quantity

while True:
    print("Enter 1 to add a store: ")
    print("Enter 2 to add item to a store: ")
    print("Enter q to quit: ")

    choice = input("Enter your choice: ")
    if choice == "1":
        store_name = input(" What grocery store would you like to shop at: " )
        store_address = input("Enter store address: ")
        grocery_store= Grocery_store(store_name, store_address)
        grocery_stores.append(grocery_store)
    
    elif choice == "2":
        for i in grocery_stores: 
            print(i.store_name)
            print(i.store_address)
            print(f'Your stores you like to shop at are {i.store_name} on {i.store_address} ')
            which_store = input("Which store do you want to add item to?: ") 
            add_item = input("What item do you want to add: ")
            price_item  = input("What is the price of the item: ")
            quantity_item = input("What is the quantity you want to buy: ")
            new_item = Items(add_item, price_item, quantity_item)
            items.append(new_item)
        
    
    # elif choice = "q"
    #     break
        



