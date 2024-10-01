####################################################################################################################################################################################

# Name: Anushree Dhananjaya and Student ID: s3955464

# Highest part attempted: "PASS LEVEL". Also, it can handle errors as mentioned in credit level for PASS LEVEL, Class Banquet is defined but not working.

# Any problems of the code or requirements that have not met : There are no problems with using text files of PASS LEVEL.

# Reflection: 
# 1. It was bit confusing at start but was able to connect through as I developed the program and it built my confidence in programming.
# 2. I was not able to figure out why import copy will be used. So, I need to explore bit on that.
# 3. CREDIT, DI and HD Level felt very diffcult for me. I felt I should have started the assignment in mid semester break.

#####################################################################################################################################################################################

import sys
import copy
import os

#Customized exceptions defined
class Error(Exception):
    """BASE CLASS EXCEPTION FOR OTHER EXCEPTIONS"""
    pass
class Validate_Quantity_Error(Error):
    """Raised when entered input is not a 0, negative or non-integer"""
    pass
class Validate_Item_Error(Error):
    """Raised when entered input is not a valid item from the given item.txt file """
    pass
class validate_registor_error(Error):
    """Raised when entered input is not valid entry for registration either for y or n / S or G"""
    pass

# Base class which acts as parent class for BRONZECUSTOMER, SILVERCUSTOMER and GOLDCUSTOMER class
class Customer: 
    
    def __init__(self,id,name):
        self.__id=id
        self.__name=name

    @property #Used to decorate the method so that it can be called using just name without using()
    def id(self):
        return self.__id

    @property 
    def name(self):
        return self.__name

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    def get_service_fee(self,cost):
        self.costs=cost
        return self.costs  

    def get_discount(self, cost):
        self.discount=cost
        return self.discount

    def display_info(self):   
        self.cust_types= "C"     
        print("customer ID: {:3}   customer name: {:8} type of customer: {:8} \n".format(self.id,self.name,self.cust_types))

#Child class of class customer
class BronzeCustomer(Customer):
    __service_fee_rate=0.1
    disc_value=0
    service_fees=0
    discount=0 

    def __init__(self,id,cust_types,name):
        super().__init__(id,name)   
        self.cust_types=cust_types

    
    @staticmethod
    def get_price(): #It is also getter method
        return BronzeCustomer.__service_fee_rate

    def get_service_fee(self,cost):
        self.costs=cost
        self.service_fees = self.get_price()*self.costs 
        return self.service_fees

    def get_discount(self, cost):
        self.costs=cost
        self.discount = self.disc_value*self.costs
        return self.discount

    def display_info(self):        
        print("customer ID: {:3}   type of customer: {:6}   customer name: {:8}  service fee rate: {:3} \n".format(self.id,self.cust_types,self.name,self.get_price()))    

    @staticmethod
    def set_price(price):
        BronzeCustomer.__service_fee_rate = price


#Child class of class customer
class SilverCustomer(Customer):
    __value=0

    def __init__(self, id,cust_types,name):
        super().__init__(id, name)
        self.service_fees=0
        self.discount=0
        self.cust_types=cust_types

    @staticmethod   
    def get_value():   #It is also getter method
        return SilverCustomer.__value
  
    def get_service_fee(self,cost):
        self.costs=cost
        self.service_fees = self.get_value()*self.costs
        return self.service_fees

    def get_discount(self, cost):
        self.costs=cost
        self.discount = self.get_value()*self.costs
        return self.discount

    def display_info(self):        
        print("customer ID: {:3}   type of customer: {:6}   customer name: {:8} service fee rate: {:3}\n".format(self.id,self.cust_types,self.name, self.get_value()))

#Child class of class customer
class GoldCustomer(Customer):

    __discount_rate=0.08
    value=0

    def __init__(self, id,cust_types,name,discounts=""):
        super().__init__(id, name)
        self.service_fees=0
        self.discounts=discounts
        self.cust_types=cust_types

    
    @staticmethod
    def discount(): #It is also getter method
        return GoldCustomer.__discount_rate

    def get_service_fee(self,cost):
        self.costs=cost
        self.service_fees = self.value*self.costs
        return self.service_fees

    def get_discount(self, cost):
        if self.discounts == ("" or 0):
            self.costs=cost
            cal = self.discount()*self.costs
        else:
            self.costs=cost
            cal = self.discounts *self.costs
        return cal

    def display_info(self):       
        print("customer ID: {:3}   type of customer: {:6}   customer name: {:8} service fee rate: {:3}  discount: {:3}\n".format(self.id,self.cust_types,self.name,self.value,self.discounts))

    @staticmethod
    def set_discount(rate):
        GoldCustomer.__discount_rate = rate

#Parent class of FoodDish and Drink class
class Item():
    def __init__(self,id="",name="",price=0):
        self.id=id
        self.name=name
        self.price=price

    def display_info(self):
        print(" id: {:3}  type: {:3} name: {:10} price: {:4}\n".format(self.id,self.name,self.price))        

#Child class of class Item
class FoodDish(Item):

    def __init__(self,id="", item_type="",name="",price=0):
        super().__init__(id,name,price)
        self.item_type=item_type

    def display_info(self):
        print(" id: {:3}  type: {:3} name: {:10} price: {:4}\n".format(self.id,self.item_type,self.name,self.price))  

#Child class of class Item
class Drink(Item):

    def __init__(self,id="", item_type="",name="",price=0):
        super().__init__(id,name,price)
        self.item_type=item_type

    def display_info(self):
        print(" id: {:3}  type: {:3} name: {:10} price: {:4}\n".format(self.id,self.item_type,self.name,self.price)) 

#Child class of class Item
class Banquet(Item):

    def __init__(self,id="", item_type="",name="",price=0, components=""):
        super().__init__(id,name,price)
        self.item_type=item_type
        self.components=components

    def display_info(self):
        print(" id: {:3}  type: {:3} name: {:10} components: {:4}\n".format(self.id,self.item_type,self.name,self.components)) 
        
#Contains details of customer orders and calculate the cost of ordered items
class Order():

    def __init__(self,customer_name="",dish_name="",quantity=""):
        self.customer_name=customer_name
        self.dish_name=dish_name
        self.quantity=quantity

    @property
    def dish_price(self):
        return self.dish_price

    #Calculates dish costs without service fee and discount     
    def compute_cost(self, dish_price,quantity,Servicefee, discount):        
        orginal_cost= dish_price * quantity
        Servicefee= Servicefee*quantity
        discount = discount*quantity
        return orginal_cost, Servicefee, discount

    #Claculates the total cost of the dish ordered by the customer
    def Total_cost(self, orginal_cost, Servicefee, discount):
        Total_cost= (orginal_cost) + (Servicefee) - (discount)
        return Total_cost

#Acts as main data repository where all data is loaded and distrubeted accross the classes
class Records():
    #list is used to store customer and item details as it is mutable
    list_existing_customers = []
    list_existing_items=[]

    #Adds the customer details to the main customer list
    def add_record_customer(self,id,cust_types,name,discounts=""):
        record= None
        if(discounts==""):
            if cust_types == "B":
                record=BronzeCustomer(id,cust_types,name)
            elif cust_types == "S":
                record=SilverCustomer(id,cust_types,name)
        elif cust_types == "G":
            record=GoldCustomer(id,cust_types,name,discounts)
        self.list_existing_customers.append(record)

    #Reads the cutomer details from the customer.txt file 
    def read_customers(self,file_name):
            input_file = open(file_name,"r")
            i=0
            line_from_file = input_file.readline()
            while(line_from_file!=""):
                fields_from_line = line_from_file.strip().split(",")
                i=0
                for item in fields_from_line:
                    item_list = item.split(':')
                    fields_from_line[i]=item_list[1].strip()
                    i+=1
                id= int(fields_from_line[0])
                cust_types = fields_from_line[1]
                name = fields_from_line[2]
                if (len(fields_from_line)<=3):
                    self.add_record_customer(id,cust_types,name)
                else: #
                    discounts=float(fields_from_line[3])
                    self.add_record_customer(id,cust_types,name,discounts)
                line_from_file=input_file.readline()
                i+=1
            input_file.close()
            return i
  
    #Adds the items details to the main customer list
    def add_record_item(self,id,item_type,name,price,components=""):
        record= None
        if(components==""):
            if item_type == "F":
                    record=FoodDish(id,item_type,name,price)
            elif item_type == "D":
                    record=Drink(id,item_type,name,price)
        elif item_type == "B":
            record=Banquet(id,item_type,name,components)
        self.list_existing_items.append(record)

    #Reads the items details from the items.txt file 
    def read_items(self,file_name):
            input_file = open(file_name,"r")
            i=0
            line_from_file = input_file.readline()
            while(line_from_file!=""):
                fields_from_line = line_from_file.strip().split(",")
                i=0
                for item in fields_from_line:
                    item_list = item.split(':')
                    fields_from_line[i]=item_list[1].strip()
                    i+=1
                id= int(fields_from_line[0])
                item_type = fields_from_line[1]
                name = fields_from_line[2]
                price= float(fields_from_line[3])
                self.add_record_item(id,item_type,name,price)
                line_from_file = input_file.readline()
            input_file.close()

    #finds if customers exists in the cutomer list or not     
    def find_customer(self,search_value):
        for i in range(len(self.list_existing_customers)):
                if search_value == self.list_existing_customers[i].name:
                    return self.list_existing_customers[i]
                elif search_value != self.list_existing_customers[i]:
                    if i == len(self.list_existing_customers) - 1:
                        return None
        
    #Identifys to which customer type the customer belongs to
    def find_customer_type(self,search_value):
        for i in range(len(self.list_existing_customers)):
                if search_value == self.list_existing_customers[i].cust_types:
                    return self.list_existing_customers[i]
                elif search_value != self.list_existing_customers[i].cust_types:
                    if i == len(self.list_existing_customers) - 1:
                        return None    

    #finds if items exists in the items list or not 
    def find_item(self, search_value):        
        for i in range(len(self.list_existing_items)):
            if search_value == self.list_existing_items[i].name:
                return self.list_existing_items[i]
            elif search_value != self.list_existing_items[i].name:
                if i == len(self.list_existing_items) - 1:
                    return None

    #Displays all customer details
    def display_customers(self):
        for i in self.list_existing_customers:
            i.display_info()

    #Displays all item details  
    def display_items(self):
        for i in self.list_existing_items:
            i.display_info()

    #Generates the unique ID for new customer 
    @property
    def generate_id(self):
        #list is used to store id as it is mutable
        new_id=[]  
        while True:   
            for i in range(len(self.list_existing_customers)):
                id_list= self.list_existing_customers[i].id
                new_id.append(id_list)
            new_id= max(new_id)+1
            return new_id

#This is the main class which acts as front end UI by collecting information from user and displaying output accordingly
class Operations:

    load_record= Records()

    #Checks for customer and item texts files.
    def Checkfile(self):
        data_file_customer="customers.txt"
        data_file_item="items.txt"
        try:
            self.load_record.read_customers(data_file_customer)
        except Exception:
            self.output_error(". Could not load from file "+data_file_customer+"\n")
            sys.exit() 
        finally:
            if(os.path.exists(data_file_item)):
                self.load_record.read_items(data_file_item)
            else:
                self.output_error(". Could not load from file "+data_file_item+"\n")
                sys.exit() 
  
        User_reply=self.get_menu_choice() 
        #To make menu appear again after task is completed.       
        while (reply!=0):               
            #navigate the user reply options to perticular function of that options       
            if reply == 1:                                                                                  
                self.User_reply_1()                                                                                                                  
            elif reply == 2:                                        
                self.User_reply_2()                              
            elif reply == 3:
                self.User_reply_3()
            User_reply=self.get_menu_choice()                     
                   
    #Error format if file does not exists 
    def output_error(self,message):
        sys.stderr.write("Problem! "+message+"\n")

    #Displays menu options to choose for resturant ordering system
    def get_menu_choice(self):
        global reply
        sys.stdout.write("\n")
        sys.stdout.write("Welcome to the RMIT resturant ordering system!\n")
        sys.stdout.write("\n")
        sys.stdout.write(48*"#"+"\n")
        sys.stdout.write("You can choose from the following options:\n")
        sys.stdout.write("1: order a meal\n")
        sys.stdout.write("2: Display existing customers information\n")
        sys.stdout.write("3: Display existing items information\n")
        sys.stdout.write("0: Exit the program\n")
        sys.stdout.write(48*"#"+"\n")
        sys.stdout.write("\n")
        reply=self.get_str("Choose one option: \n")

    #Checks if entered option input is blank or not
    def get_str(self,prompt):
            sys.stdout.write(prompt)
            sys.stdout.flush()
            value=int(sys.stdin.readline().strip())
            while( value<0 ):
                sys.stdout.write("Input cannot be blank. Re-enter: ")
                sys.stdout.flush()
                value=sys.stdin.readline().strip()
            return value

    #Finds the dish price for coressponding dish name
    @property
    def dish_price(self):
        load_record = Records()
        Available_dish_name= load_record.list_existing_items
        for i in range(len(Available_dish_name)):
            if dish_name == Available_dish_name[i].name:
                dish_price = Available_dish_name[i].price
                return dish_price
            
    #option 1: where customer can order a meal  
    def User_reply_1(self):        
        #as these variables where not accessible outside function
        global dish_name,quantity,customer_name
        customer_list = Records()  
        sys.stdout.write("Enter the name of the Customer [e.g. Kate, Tom]:\n")
        customer_name=sys.stdin.readline().strip()
        dish_name=self.validate_dish("Enter the name of the dish [enter a vaild dish only, e.g. hamburger, coke, pizza]:\n")
        quantity=self.validate_quantity("Enter the dish quantity [enter a positive integer only, e.g. 1, 2, 3]:\n")
        customer = customer_list.find_customer(customer_name)
        calculatecost = Order()

        #Checks if customer is new or existing 
        if customer is None:
            sys.stdout.write("This is a new customer. Does customer want to join the rewards program [enter y or n]?\n")
            reply=sys.stdin.readline().strip()            
            tocheck =True

            #Checks if user entered correct input 'y' or 'n' and to display iteratively if entered input is wrong
            while tocheck:                
                if reply == 'y':
                    sys.stdout.write("What kind of rewards the customer wants [enter S or G]?\n")
                    userreply= sys.stdin.readline().strip()
                    tocheck1 =True

                    #Checks if user entered correct input 'S' or 'G' and to display iteratively if entered input is wrong
                    while tocheck1:
                        userreply= customer_list.find_customer_type(userreply)


                        if isinstance(userreply, SilverCustomer):
                            #should have 48 * in receipt at start and after customer name is displayed
                            sys.stdout.write(51*"*"+"\n")    
                            sys.stdout.write("Receipt of Customer"' '+customer_name+"\n")
                            sys.stdout.write(51*"*"+"\n")
                            Servicefee= userreply.get_service_fee(self.dish_price)
                            discount = userreply.get_discount(self.dish_price)
                            dish_price = self.dish_price
                            Registration_fee= 100.0
                            id= customer_list.generate_id                           
                            orginal_cost, Servicefee, discount = calculatecost.compute_cost(dish_price , quantity , Servicefee, discount)                        
                            sys.stdout.write(f'{dish_name:<16}' ":"f'{(self.dish_price):>22}'' ' "AUD"' '"x"' ' +f'{quantity:>5}'+"\n") 
                            sys.stdout.write("Service fee"' '' '' '' '' '":" +str(round(Servicefee,2)).rjust(28)+' ' '(AUD)'"\n") 
                            sys.stdout.write("Registration fee:" +str(round(Registration_fee,2)).rjust(28)+' ' '(AUD)'"\n")                            
                            Total_cost= calculatecost.Total_cost(orginal_cost, Servicefee, discount) + Registration_fee
                            sys.stdout.write("Total cost"' ' ' ' ' '' ' ' '' '":" +str(round(Total_cost,2)).rjust(28)+' ' '(AUD)'"\n")
                            customer_list.add_record_customer(id,'S',customer_name)
                            break

                        elif isinstance(userreply, GoldCustomer):
            
                            #should have 48 * in receipt at start and after customer name is displayed
                            sys.stdout.write(51*"*"+"\n")    
                            sys.stdout.write("Receipt of Customer"' '+customer_name+"\n")
                            sys.stdout.write(51*"*"+"\n")
                            Servicefee= userreply.get_service_fee(self.dish_price)
                            discount = userreply.get_discount(self.dish_price)
                            dish_price = self.dish_price
                            Registration_fee= 300.0
                            id= customer_list.generate_id
                            orginal_cost, Servicefee, discount = calculatecost.compute_cost(dish_price , quantity , Servicefee, discount)                       
                            sys.stdout.write(f'{dish_name:<16}' ":"f'{(self.dish_price):>22}'' ' "AUD"' '"x"' ' +f'{quantity:>5}'+"\n") 
                            sys.stdout.write("Service Fee"' '' '' '' '' '":" +str(round(Servicefee,2)).rjust(28)+' ' '(AUD)'"\n") 
                            sys.stdout.write("Registration fee:" +str(round(Registration_fee,2)).rjust(28)+' ' '(AUD)'"\n") 
                            sys.stdout.write("Discount"' '' '' '' '' '' '' '' '":" +str(round(discount,2)).rjust(28)+' ' '(AUD)'"\n")                            
                            Total_cost= calculatecost.Total_cost(orginal_cost, Servicefee, discount) + Registration_fee
                            sys.stdout.write("Total cost"' ' ' ' ' '' '' '' '":" +str(round(Total_cost,2)).rjust(28)+' ' '(AUD)'"\n")
                            customer_list.add_record_customer(id,'G',customer_name,userreply.discount())
                            break

                        else:
                            try:
                                if userreply != ('S' or 'G'):
                                    raise validate_registor_error
                            
                            except validate_registor_error:
                                sys.stdout.write("This is not valid entry.Please enter [ S or G] \n") 
                                userreply=sys.stdin.readline().strip()
                                tocheck1 =True
                    break

                elif reply == 'n':
                
                    customer= 'B'
                    customer= customer_list.find_customer_type(customer)
                    if isinstance(customer, BronzeCustomer):                            
                        Servicefee= customer.get_service_fee(self.dish_price)
                        dish_price = self.dish_price
                        discount = customer.get_discount(self.dish_price)
                        id= customer_list.generate_id
                        orginal_cost, Servicefee, discount = calculatecost.compute_cost(dish_price , quantity , Servicefee, discount)
                        #should have 48 * in receipt at start and after customer name is displayed
                        sys.stdout.write(51*"*"+"\n")    
                        sys.stdout.write("Receipt of Customer"' '+customer_name+"\n")
                        sys.stdout.write(51*"*"+"\n")
                        sys.stdout.write(f'{dish_name:<13}' ":"f'{(self.dish_price):>20}'' ' "AUD"' '"x"' ' +f'{quantity:>7}'+"\n") 
                        sys.stdout.write("Service Fee"' '' '":" +str(round(Servicefee,2)).rjust(28)+' ' '(AUD)'"\n") 
                        Total_cost= calculatecost.Total_cost(orginal_cost, Servicefee, discount)
                        sys.stdout.write("Total cost"' ' ' ' ' '":" +str(round(Total_cost,2)).rjust(28)+' ' '(AUD)'"\n")
                        customer_list.add_record_customer(id,'B',customer_name)
                        break
                else:
                    try:
                       if reply != ('y' or 'n'):
                        raise validate_registor_error
                    
                    except validate_registor_error:
                        sys.stdout.write("This is not valid entry.Please enter [ y or n] \n") 
                        reply=sys.stdin.readline().strip()
                        tocheck =True
            
        else :    

            if isinstance(customer, BronzeCustomer) :
                    Servicefee= customer.get_service_fee(self.dish_price)
                    dish_price = self.dish_price
                    discount = customer.get_discount(self.dish_price)
                    orginal_cost, Servicefee, discount = calculatecost.compute_cost(dish_price , quantity , Servicefee, discount)
                    sys.stdout.write("Belongs to Customer Type: Bronze\n")
                    sys.stdout.write(51*"*"+"\n")    
                    sys.stdout.write("Receipt of Customer"' '+customer_name+"\n")
                    sys.stdout.write(51*"*"+"\n")
                    sys.stdout.write(f'{dish_name:<13}' ":"f'{(self.dish_price):>20}'' ' "AUD"' '"x"' ' +f'{quantity:>7}'+"\n") 
                    sys.stdout.write("Service Fee"' '' '":" +str(round(Servicefee,2)).rjust(28)+' ' '(AUD)'"\n") 
                    Total_cost= calculatecost.Total_cost(orginal_cost, Servicefee, discount)
                    sys.stdout.write("Total cost"' ' ' ' ' '":" +str(round(Total_cost,2)).rjust(28)+' ' '(AUD)'"\n")

            elif isinstance(customer, SilverCustomer):

                    Servicefee= customer.get_service_fee(self.dish_price)
                    discount = customer.get_discount(self.dish_price)
                    dish_price = self.dish_price
                    orginal_cost, Servicefee, discount = calculatecost.compute_cost(dish_price , quantity , Servicefee, discount)
                    sys.stdout.write("Belongs to Customer Type: Silver\n")
                    sys.stdout.write(51*"*"+"\n")    
                    sys.stdout.write("Receipt of Customer"' '+customer_name+"\n")
                    sys.stdout.write(51*"*"+"\n")              
                    sys.stdout.write(f'{dish_name:<13}' ":"f'{(self.dish_price):>20}'' ' "AUD"' '"x"' ' +f'{quantity:>7}'+"\n") 
                    sys.stdout.write("Service Fee"' '' '":" +str(round(Servicefee,2)).rjust(28)+' ' '(AUD)'"\n")                   
                    Total_cost= calculatecost.Total_cost(orginal_cost, Servicefee, discount)
                    sys.stdout.write("Total cost"' ' ' ' ' '":" +str(round(Total_cost,2)).rjust(28)+' ' '(AUD)'"\n")

            elif isinstance(customer, GoldCustomer) :

                    Servicefee= customer.get_service_fee(self.dish_price)
                    discount = customer.get_discount(self.dish_price)
                    dish_price = self.dish_price
                    orginal_cost, Servicefee, discount = calculatecost.compute_cost(dish_price , quantity , Servicefee, discount)    
                    sys.stdout.write("Belongs to Customer Type: Gold\n")
                    sys.stdout.write(51*"*"+"\n")    
                    sys.stdout.write("Receipt of Customer"' '+customer_name+"\n")
                    sys.stdout.write(51*"*"+"\n")                
                    sys.stdout.write(f'{dish_name:<13}' ":"f'{(self.dish_price):>20}'' ' "AUD"' '"x"' ' +f'{quantity:>7}'+"\n") 
                    sys.stdout.write("Service Fee"' '' '":" +str(round(Servicefee,2)).rjust(28)+' ' '(AUD)'"\n") 
                    sys.stdout.write("Discount"' '' '' '' '' '":" +str(round(discount,2)).rjust(28)+' ' '(AUD)'"\n")                 
                    Total_cost= calculatecost.Total_cost(orginal_cost, Servicefee, discount)
                    sys.stdout.write("Total cost"' ' ' ' ' '":" +str(round(Total_cost,2)).rjust(28)+' ' '(AUD)'"\n")

     #reads and checks if user entered the dish present in the item list
    def validate_dish(self,prompt): 
        sys.stdout.write(prompt)
        sys.stdout.flush()
        value=sys.stdin.readline().strip()
        itemlist = Records()
        itemname = itemlist.find_item(value)

        while (value != itemname):
            try:
                if isinstance(itemname, FoodDish):
                    return value 
                elif isinstance(itemname, Drink):
                    return value 
                else:
                    raise Validate_Item_Error()
            except Validate_Item_Error:
                sys.stdout.write("Item is invalid. Please enter a valid item! \n")
                value=sys.stdin.readline().strip()
                itemname = itemlist.find_item(value)               
        return value  

    #reads and checks if user entered the quantity is not 0 or negative
    def validate_quantity(self,prompt): 
        quantity_true= True
        #Used while loop iteratively for every wrong answer until vaild positive number is entered
        while(quantity_true):
            try:
                sys.stdout.write(prompt)
                sys.stdout.flush()
                value=float(sys.stdin.readline().strip()) 
                if value > 0:
                    return value
                else:
                    raise Validate_Quantity_Error()
            except Validate_Quantity_Error:
                sys.stdout.write("This quantity is not valid\n") 
                quantity_true= True
            except ValueError:
                sys.stdout.write("This quantity is not valid\n") 
                quantity_true= True

    #option 2: to display existing customer information from the customer text file  
    def User_reply_2(self):
        showcustomer= Records()
        showcustomer.display_customers()

    #option 3: to display existing items information from the items text file 
    def User_reply_3(self):    

        showitem= Records()
        showitem.display_items() 

    #option 0: to exit from the iterative loop or to quit from the menu
    def User_reply_0(self):
        # [7]P. SystemExit, "Python SystemExit | How Python SystemExit Work with Examples", EDUCBA, 2022. [Online]. Available: https://www.educba.com/python-systemexit/. [Accessed: 28- Aug- 2022].
        try: 
            sys.exit("Thank You")   
        except BaseException:
            print("Exited from RMIT resturant ordering system")
    
calling_main= Operations()
calling_main.Checkfile()

        