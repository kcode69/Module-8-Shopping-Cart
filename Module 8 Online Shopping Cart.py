#Module 8
#Kirk Heck

#class item for storing item name, description, price and quantity
class ItemsToPurchase:
    def __init__(self, item_name ='none' , item_description = 'none', item_price = float(0.0), item_quantity = int(0)):
        
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity
        

    def print_item_cost(item):

        subtotal = item.item_quantity*item.item_price
        print(item.item_name, item.item_quantity,'@ $',f'{item.item_price:.2f}', '= $', f'{subtotal:.2f}')
        return subtotal
    
    def print_item_description(source):
        print(source.item_name,': ',source.item_description)
    
#class for storing and manipulating shoping carta
class Shopping_Cart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []


    def add_items(cart, item_to_purchase, description, price, qty):
            
                #creat object 
                item = ItemsToPurchase(item_to_purchase, description, price, qty)
                
                #append item object to cart_items list
                cart.cart_items.append(item)
                
                
        
                    

    def remove_items(cart,item_remove):
     
        for j in range(0, len(cart.cart_items)):
            #remove str item if found in object list
            if item_remove == cart.cart_items[j].item_name:
                
                cart.cart_items.pop(j)
                return
    
        #for loop did not find a match, back to main menue
        print('Item not found and not removed/change from list\nBack to main menue.')
                
                

    
    #Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    #If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
    #If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
    def modify_item(cart, item_to_modify,modify_quantity):
        
        for i in range(0, cart.get_num_items_in_cart()):
           
            if (item_to_modify == cart.cart_items[i].item_name):
                
                #get description/price found cart_item in list
                description = cart.cart_items[i].item_description
                price = cart.cart_items[i].item_price

                #remove found cart_item[i] from list
                cart.cart_items.pop(i)

                #create new old object
                cart.add_items(item_to_modify, description,price, modify_quantity)
                
            else:
                print("Nothing found and nothing removed. Back to main menue.")    
        
    
    #Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        num_items = 0
        
        num_items = len(self.cart_items)
        return num_items
        

    #Outputs total of objects in cart.    
    #If cart is empty, output this message: SHOPPING CART IS EMPTY
    def print_total(cart):
        #print('this is print total')
        numcart = cart.get_num_items_in_cart()
        total = 0.0
        for i in range(0, numcart):
            
            subtotal = cart.cart_items[i].print_item_cost()
            total = float(total) + float(subtotal)

        if total == 0.0:
            print('SHOPING CART IS EMPTY')
        else:
            print('\nTotal for today is:', f'{total:.2f}')

    #Outputs each item's description.    
    def print_descriptions(cart):

        numcart = cart.get_num_items_in_cart()

        for i in range(0, numcart):
            item = cart.cart_items[i]
            #print('item is', item)
            item.print_item_description()


def print_menu(cart):
    while True:
        print("\nCustomer Name:", cart.customer_name,"\nToday's date:", cart.current_date)

        print('       Menu:\n',
             'a - Add item to cart\n',
             'r - Remove item from cart\n',
             'c - Change item quantity\n',
             'i - Output item description\n',
             'o - Output shopping cart\n',
             'q - Quit\n',
             'Chose an option:')
        
        option = input()

        if option == 'q':
            print('Have a nice day')
            return False
        
        elif option == 'a': 

            item_to_purchase = 'none'
            while item_to_purchase != '0':

                if item_to_purchase != '0':
                    print('What item would you like to add? Enter 0 to exit')
                    item_to_purchase = str(input())
                    
                #break while loop if input is '0'
                if item_to_purchase == '0':
                    break

                print('What is the description of ', item_to_purchase)
                description = str(input())

                print('How many ',item_to_purchase, 'are you purchasing?')
                qty = int(input())

                print('What is the price of', item_to_purchase, '?')
                price = float(input())

                #add_items method
                cart.add_items(item_to_purchase, description, price, qty)

            
        elif option == 'r':
            print('\nYour cart contains:')   
            for i in range(0, len(cart.cart_items)):
                print(cart.cart_items[i].item_name)
        
            print("\nWhat item would you like to remove?")
            item_remove = str(input())            
            cart.remove_items(item_remove)
        
        elif option == 'c':
            print('Changing item quantity')
            print('Cart contains:')

            if int(cart.get_num_items_in_cart()) != int(0):   
                
                try:
                    for i in range(0,cart.get_num_items_in_cart()):
                        print('Item Name:', cart.cart_items[i].item_name, ' Quantity:', cart.cart_items[i].item_quantity)
                    
                    item_to_change = str(input('Enter the name of the item to change\n'))
                    modify_quantity = int(input('Enter the new quantity\n'))
                    
                except ValueError:
                    print('Invalid entry')

                cart.modify_item(item_to_change, modify_quantity)
            else:
                print('Cart is empty. Back to menue')

        elif option == 'i':
            print(cart.customer_name,' - ',cart.current_date)
            print('Descripsion of Items in cart:')

            cart.print_descriptions()
        
        elif option == 'o':
            print('Total for shoping cart')
            print(cart.customer_name,' - ',cart.current_date)
            cart.print_total()

        else:
            print("Invalid option try again.")
def main():
    customer_name = str(input('Hello, what is your name? '))
    current_date = str(input('What is todays date? '))
    cart = Shopping_Cart(customer_name, current_date)
    print_menu(cart)

#impliment main()
main()
            


