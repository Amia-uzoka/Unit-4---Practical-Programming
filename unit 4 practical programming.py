def read_data(filename): #read vendor data from text file and store them
    
    data = [] # dataset

    with open(filename, "r") as file: #with statement makes sure file is closed after use
        lines = file.readlines() #The readlines() method returns a list containing each line in the file as a list item.

        for item in lines:
            columns = item.strip().split(",")
            
        
            row = [
                
                columns[0], #vendor ID
                columns[1], #Vendor name 
                columns[2], # year and week 
                int(columns[3]), #number of vegan hotdogs 
                int(columns[4]), # Number of meat hotdogs 
                float(columns[5]), # Onions(Kg)
                float(columns[6]), # Ketchup (litres)
                

                     ]
            data.append(row)
    for row in data:
                print(row)
    return data
print(read_data("Hotdogs (1).txt"))
hotdog_data = read_data("Hotdogs (1).txt")
#linear search
def linear_search_unsorted(data, target):

    for row in hotdog_data:
        if row[1].lower() == target.lower():
         
            return row
        
    return None
result = linear_search_unsorted(hotdog_data, "korner kart")
if result is None:
    print("vendor not found")

else:
        print("Vendor ID:", result[0])
        print("Vendor name:", result[1])
        print("Year and Week:", result[2])
        print("Number of vegan hotdogs:", result[3])
        print("Number of meat hotdogs:", result[4])
        print("Onions (Kg):", result[5])
        print("Ketchup (Litres):", result[6])




def read_data(filename): #read vendor data from text file and store them
    
    data = [] # dataset
    try:

        with open(filename, "r") as file: #with statement makes sure file is closed after use
            lines = file.readlines() #The readlines() method returns a list containing each line in the file as a list item.

    except FileNotFoundError:
         print("File not found")

        
    for item in lines:
            columns = item.strip().split(",")
            
        
            row = [
                
                columns[0], #vendor ID
                columns[1], #Vendor name 
                columns[2], # year and week 
                int(columns[3]), #number of vegan hotdogs 
                int(columns[4]), # Number of meat hotdogs 
                float(columns[5]), # Onions(Kg)
                float(columns[6]), # Ketchup (litres)
                

                     ]
            data.append(row)

            
    # Unit test 1
    # Test 1
    #for row in data:
        #print(row)
    # Test 2
    #print(data[9][0])
    # Test3
    
    
    
        
    return data
    

hotdog_data = read_data("Hotdogs (1).txt")









#linear search
def linear_search_unsorted(data, target):
    
    for row in hotdog_data:
        if row[1].lower() == target.lower():
         
            return row
        
    return None

try:
    user_input = input("Search Vendors")
    
    if not user_input or not all(c.isalpha() or c.isspace() for c in user_input):
        raise ValueError
    
    result = linear_search_unsorted(hotdog_data, user_input)
    
    if result is None:
        print("vendor not found")

    else:
            print("Vendor ID:", result[0])
            print("Vendor name:", result[1])
            print("Year and Week:", result[2])
            print("Number of vegan hotdogs:", result[3])
            print("Number of meat hotdogs:", result[4])
            print("Onions (Kg):", result[5])
            print("Ketchup (Litres):", result[6])
            
except ValueError:
    print("invalid input")

#bubble sort
    def bubble_sort(data):
        new_data = data.copy()
        for i in range(len(new_data)):
            for j in range 

import sys

def read_data(filename): #read vendor data from text file and store them
    
    data = [] # dataset
    try:

        with open(filename, "r") as file: #with statement makes sure file is closed after use
            lines = file.readlines() #The readlines() method returns a list containing each line in the file as a list item.

    except FileNotFoundError:
         print("File not found")

        
    for item in lines:
            columns = item.strip().split(",")
            
        
            row = [
                
                columns[0], #vendor ID
                columns[1], #Vendor name 
                columns[2], # year and week 
                int(columns[3]), #number of vegan hotdogs 
                int(columns[4]), # Number of meat hotdogs 
                float(columns[5]), # Onions(Kg)
                float(columns[6]), # Ketchup (litres)
                

                     ]
            data.append(row)

            
    # Unit test 1
    # Test 1
    #for row in data:
        #print(row)
    # Test 2
    #print(data[9][0])
    # Test3
    
    
    
        
    return data
    

hotdog_data = read_data("Hotdogs (1).txt")

import sys

def read_data(filename): #read vendor data from text file and store them
    
    data = [] # dataset
    
    try:

        with open(filename, "r") as file: #with statement makes sure file is closed after use
            lines = file.readlines() #The readlines() method returns a list containing each line in the file as a list item.

    except FileNotFoundError:
         print(" Error: File not found")

        
    for item in lines:
            columns = item.strip().split(",")
            
        
            row = [
                
                columns[0], #vendor ID
                columns[1], #Vendor name 
                columns[2], # year and week 
                int(columns[3]), #number of vegan hotdogs 
                int(columns[4]), # Number of meat hotdogs 
                float(columns[5]), # Onions(Kg)
                float(columns[6]), # Ketchup (litres)
                

                     ]
            data.append(row)

            
    # Unit test 1
    # Test 1
    #for row in data:
        #print(row)
    # Test 2
    #print(data[9][0])
    # Test3
    
    
    
        
    return data
    

hotdog_data = read_data("Hotdogs (1).txt")









#linear search
def linear_search_unsorted(data, target):
    
    for row in hotdog_data:
        if row[1].lower() == target.lower():
         
            return row
        
    return None

try:
    user_input = input("Search Vendors")
    
    if not user_input or not all(c.isalpha() or c.isspace() for c in user_input):
        raise ValueError
    
    result = linear_search_unsorted(hotdog_data, user_input)
    
    if result is None:
        print("vendor not found")

    else:
            print("Vendor ID:", result[0])
            print("Vendor name:", result[1])
            print("Year and Week:", result[2])
            print("Number of vegan hotdogs:", result[3])
            print("Number of meat hotdogs:", result[4])
            print("Onions (Kg):", result[5])
            print("Ketchup (Litres):", result[6])
            
except ValueError:
    print("invalid input")

#bubble sort
def bubble_sort(data):
    new_data = data.copy() # minimises risk of losing original data 
    
    for i in range(len(new_data)):#?
        
        for j in range(len(new_data) -1): # inner loop looks goes through each list in our dataset
            
            swapped = False
            
            if new_data[j][1].lower() > new_data[j+1][1].lower(): # take one list(J) within the dataset look at index one (vendor name) compare it to index one (vendor name) in the following list[J + 1) 

                new_data[j], new_data[j + 1] = new_data[j + 1], new_data[j] #If j / first value is alhabetically higher than the next value swap them 

                swapped = True # update status of list 
                
            if not swapped:
                break
            
        return new_data #store the newly sorted dataset
    
bubble_sorted_data = bubble_sort(hotdog_data)
user_input_view_sorted_file = input("Do you want to see the sorted file yes/no?")
if user_input_view_sorted_file.lower()== "yes": #allow user option to see sorted file if they wish 
    for row in sorted_data:
        print(row)
else:
    exit








#linear search
def linear_search_unsorted(data, target):
    
    for row in hotdog_data:
        if row[1].lower() == target.lower():
         
            return row
        
    return None

try:
    user_input = input("Search Vendors")
    
    if not user_input or not all(c.isalpha() or c.isspace() for c in user_input):
        raise ValueError
    
    result = linear_search_unsorted(hotdog_data, user_input)
    
    if result is None:
        print("vendor not found")

    else:
            print("Vendor ID:", result[0])
            print("Vendor name:", result[1])
            print("Year and Week:", result[2])
            print("Number of vegan hotdogs:", result[3])
            print("Number of meat hotdogs:", result[4])
            print("Onions (Kg):", result[5])
            print("Ketchup (Litres):", result[6])
            
except ValueError:
    print("invalid input")

#bubble sort
def bubble_sort(data):
    new_data = data.copy() # minimises risk of losing original data 
    
    for i in range(len(new_data)):#?
        
        for j in range(len(new_data) -1): # Take j as each list within the dataset (look through list from left to right compare items side by side)
            swapped = False
            
            if new_data[j][1].lower() > new_data[j+1][1].lower(): # take one list(J) within the dataset look at index one (vendor name) compare it to index one in the following list[J + 1) if 

                new_data[j], new_data[j + 1] = new_data[j + 1], new_data[j]

                swapped = True
            if not swapped:
                break
        return new_data
    
sorted_data = bubble_sort(hotdog_data)
user_input_view_sorted_file = input("Do you want to see the sorted file yes/no?")
if user_input_view_sorted_file.lower()== "yes":
    for row in sorted_data:
        print(row)
else:
    exit




import sys

def read_data(filename): #read vendor data from text file and store them
    
    data = [] # dataset
    
    try:

        with open(filename, "r") as file: #with statement makes sure file is closed after use
            lines = file.readlines() #The readlines() method returns a list containing each line in the file as a list item.

    except FileNotFoundError:
         print(" Error: File not found")

        
    for item in lines:
            columns = item.strip().split(",")
            
        
            row = [
                
                columns[0], #vendor ID
                columns[1], #Vendor name 
                columns[2], # year and week 
                int(columns[3]), #number of vegan hotdogs 
                int(columns[4]), # Number of meat hotdogs 
                float(columns[5]), # Onions(Kg)
                float(columns[6]), # Ketchup (litres)
                

                     ]
            data.append(row)

            
    # Unit test 1
    # Test 1
    #for row in data:
        #print(row)
    # Test 2
    #print(data[9][0])
    # Test3
    
    
    
        
    return data
    

hotdog_data = read_data("Hotdogs (1).txt")









#linear search
def linear_search_unsorted(data, target):
    
    for row in hotdog_data:
        if row[1].lower() == target.lower():
         
            return row
        
    return None

try:
    user_input = input("Search Vendors")
    
    if not user_input or not all(c.isalpha() or c.isspace() for c in user_input): # checks through every character in user input and 
        raise ValueError
    
    result = linear_search_unsorted(hotdog_data, user_input)
    
    if result is None:
        print("vendor not found")

    else:
            print("Vendor ID:", result[0])
            print("Vendor name:", result[1])
            print("Year and Week:", result[2])
            print("Number of vegan hotdogs:", result[3])
            print("Number of meat hotdogs:", result[4])
            print("Onions (Kg):", result[5])
            print("Ketchup (Litres):", result[6])
            
except ValueError:
    print("invalid input")

#bubble sort
def bubble_sort(data):
    new_data = data.copy() # minimises risk of losing original data 
    
    for i in range(len(new_data)):#?
        
        for j in range(len(new_data) -1): # inner loop looks goes through each list in our dataset
            
            swapped = False
            
            if new_data[j][1].lower() > new_data[j+1][1].lower(): # take one list(J) within the dataset look at index one (vendor name) compare it to index one (vendor name) in the following list[J + 1) 

                new_data[j], new_data[j + 1] = new_data[j + 1], new_data[j] #If j / first value is alhabetically higher than the next value swap them 

                swapped = True # update status of list 
                
            if not swapped:
                break
            
        return new_data #store the newly sorted dataset
    
bubble_sorted_data = bubble_sort(hotdog_data)
user_input_view_sorted_file = input("Do you want to see the sorted file yes/no?")
if user_input_view_sorted_file.lower()== "yes": #allow user option to see sorted file if they wish 
    for row in bubble_sorted_data:
        print(row)
else:
    exit
    #--------------------------------------------------------------------------------------------------------------------------------------------
    from datetime import date
import sys


def read_data(filename): #read vendor data from text file and store them
    
    data = [] # dataset
    
    try:

        with open(filename, "r") as file: #with statement makes sure file is closed after use
            lines = file.readlines() #The readlines() method returns a list containing each line in the file as a list item.

    except FileNotFoundError:
         print(" Error: File not found")

        
    for item in lines:
            columns = item.strip().split(",")
            
        
            row = [
                
                columns[0], #vendor ID
                columns[1], #Vendor name 
                columns[2], # year and week 
                int(columns[3]), #number of vegan hotdogs 
                int(columns[4]), # Number of meat hotdogs 
                float(columns[5]), # Onions(Kg)
                float(columns[6]), # Ketchup (litres)
                

                     ]
            data.append(row)

            
    # Unit test 1
    # Test 1
    #for row in data:
        #print(row)
    # Test 2
    #print(data[9][0])
    # Test3
    
    
    
        
    return data
    

hotdog_data = read_data("Hotdogs (1).txt")
#-----------------------------------------------------------------------------------------------------------------------------
def linear_search_unsorted(data):
    target = input("Search Vendors")
    
    for row in hotdog_data:
        if row[1].lower() == target.lower():
         
           
            print("Vendor ID:", row[0])
            print("Vendor name:", row[1])
            print("Year and Week:", row[2])
            print("Number of vegan hotdogs:", row[3])
            print("Number of meat hotdogs:", row[4])
            print("Onions (Kg):", row[5])
            print("Ketchup (Litres):", row[6])
            return       
    else:
        print("vendor not found")

               
#linear_search_unsorted(hotdog_data)


#linear search nyw (name year week)
def linear_search_unsorted_nyw(data):
    target_name = input("Search Vendors")
    target_yw = int(input("enter year week in format yyyywwww"))
    
    for row in hotdog_data:
        if row[1].lower() == target_name.lower() and int(row[2])== target_yw:
         
            
            print("Vendor ID:", row[0])
            print("Vendor name:", row[1])
            print("Year and Week:", row[2])
            print("Number of vegan hotdogs:", row[3])
            print("Number of meat hotdogs:", row[4])
            print("Onions (Kg):", row[5])
            print("Ketchup (Litres):", row[6])
            return
        

    print("vendor not found")


               
#linear_search_unsorted_nyw(hotdog_data)



def search_menu(data):
    print( "Option 1 search by vendor name")
    print("option 2 search by vendor name, year and week")

    choice = int(input("enter choice 1 or 2"))

    if choice == 1 :
        linear_search_unsorted(hotdog_data)

    elif choice == 2 :
        linear_search_unsorted_nyw(hotdog_data)
    else:
        print("invalid option")
#-----------------------------------------        

search_menu(hotdog_data)
#----------------------------------------



        

def add_vendor(data):
    
    vendor_id = input("Enter vendor id in the format - XX_DDD - ").upper()
    
    if len(vendor_id) <6 or len(vendor_id) > 6:
        print("invalid year and week")

        
    f_alpha_vendor_id = vendor_id [0:2]
    f_numb_vendor_id = vendor_id [4:6]
    f_u_vendor_id = vendor_id [3]
     
    
    if int(f_numb_vendor_id).isdigit() == False or f_alpha_vendor_id.isalpha == False or f_u_vendor_id != "_" :
        print("invalid vendor id given")

    
    
#-----------------------------------------------------------------------------
    #validation
    name_valid = True
 
    try:
        vendor_name = input("Enter vendor name in format")
 
        if not vendor_name or not all(c.isalpha() or c.isspace() for c in vendor_name):
            raise ValueError
        if len(vendor_name) < 2 or len(vendor_name) > 25:
            print("Invalid vendor name")
            name_valid = False
    except ValueError:
        print("invalid vendor name")
        name_valid = False
        
            
        
# -----------------------------------------------------------------------------------------

    year_week = input("Year and week of info in format [ YYYYWW ] ")
    if len(year_week) < 7  or  len(vendor_id) > 7:
        print("invalid year and week")
        
    #format_check_yw = year_week.split("-")
    current_year = date.today().year()
    
    formatweek = year_week [4:6]
    formatyear = year_week [0:3]
    
    if int(formatweek) < 1 or int(formatweek) > 52 and int(formatyear) > current_year:
        print("invalid year and week given please enter in the correct format")
  
    
#-------------------------------------------------------------------------------------------

   number_of_vegan = input("Enter number of vegan hotdogs in format ")
    
                  number_of_meat_hotdogs = input("Enter number of meatdogs in format ")
    
    onions = float(input("Enter Kg of onions "))
    
    ketchup = float(input("Enter ketchup in litres "))
    
    new_vendor = [
        
        vendor_id,
        vendor_name,
        number_of_vegan,
        number_of_meat_hotdogs,
        onions,
        ketchup
        
        ]
    print(new_vendor)
    user 
    corret_vendor_data =
    safe_data = data.copy
    safe_data.append(new_vendor)
    print("Vendor added")
  

add_vendor(hotdog_data)

print(hotdog_data)
#---------------------------------------------------------------------------------------------------------------------
from datetime import date
import sys


def read_data(filename): #read vendor data from text file and store them
    
    data = [] # dataset
    
    try:

        with open(filename, "r") as file: #with statement makes sure file is closed after use
            lines = file.readlines() #The readlines() method returns a list containing each line in the file as a list item.

    except FileNotFoundError:
         print(" Error: File not found")

        
    for item in lines:
            columns = item.strip().split(",")
            
        
            row = [
                
                columns[0], #vendor ID
                columns[1], #Vendor name 
                columns[2], # year and week 
                int(columns[3]), #number of vegan hotdogs 
                int(columns[4]), # Number of meat hotdogs 
                float(columns[5]), # Onions(Kg)
                float(columns[6]), # Ketchup (litres)
                

                     ]
            data.append(row)

                 
    return data
    

hotdog_data = read_data("Hotdogs (1).txt")
#-----------------------------------------------------------------------------------------------------------------------------
def linear_search_unsorted(data):
    target = input("Search Vendors")
    
    for row in hotdog_data:
        if row[1].lower() == target.lower():
         
           
            print("Vendor ID:", row[0])
            print("Vendor name:", row[1])
            print("Year and Week:", row[2])
            print("Number of vegan hotdogs:", row[3])
            print("Number of meat hotdogs:", row[4])
            print("Onions (Kg):", row[5])
            print("Ketchup (Litres):", row[6])
            return       
    else:
        print("vendor not found")

               
#linear_search_unsorted(hotdog_data)

#-------------------------------------------------------------------------------------------------------------------
#linear search nyw (name year week)
def linear_search_unsorted_nyw(data):
    target_name = input("Search Vendors")
    target_yw = int(input("enter year week in format yyyywwww"))
    
    for row in hotdog_data:
        if row[1].lower() == target_name.lower() and int(row[2])== target_yw:
         
            
            print("Vendor ID:", row[0])
            print("Vendor name:", row[1])
            print("Year and Week:", row[2])
            print("Number of vegan hotdogs:", row[3])
            print("Number of meat hotdogs:", row[4])
            print("Onions (Kg):", row[5])
            print("Ketchup (Litres):", row[6])
            return
        

    print("vendor not found")


               
#linear_search_unsorted_nyw(hotdog_data)



def search_menu(data):
    print( "Option 1 search by vendor name")
    print("option 2 search by vendor name, year and week")

    choice = int(input("enter choice 1 or 2"))

    if choice == 1 :
        linear_search_unsorted(hotdog_data)

    elif choice == 2 :
        linear_search_unsorted_nyw(hotdog_data)
    else:
        print("invalid option")
#----------------------------------------------------------------------------------------------------        

search_menu(hotdog_data)
#--------------------------------------------------------------------------------------------


        

def add_vendor(data):
    while True:
        vendor_id = input("Enter vendor id in the format - XX_DDD - ").upper()
        if len(vendor_id) <6 or len(vendor_id) > 6:
            print("invalid year and week")

            
        f_alpha_vendor_id = vendor_id [0:2]
        f_numb_vendor_id = vendor_id [4:6]
        f_u_vendor_id = vendor_id[3]
         
        
        if f_numb_vendor_id.isdigit() == False or f_alpha_vendor_id.isalpha == False or f_u_vendor_id != "_" :
            print("invalid vendor id given")
       

    
    
#-----------------------------------------------------------------------------
    #validation
    name_valid = True
    while True:
        try:
            vendor_name = input("Enter vendor name in format")
     
            if not vendor_name or not all(c.isalpha() or c.isspace() for c in vendor_name):
                raise ValueError
            if len(vendor_name) < 2 or len(vendor_name) > 25:
                print("Invalid vendor name")
                name_valid = False
        except ValueError:
            print("invalid vendor name")
            name_valid = False
       
            
        
# -----------------------------------------------------------------------------------------
    while True:
        year_week = input("Year and week of info in format [ YYYYWW ] ")
        if len(year_week) < 7  or  len(vendor_id) > 7:
            print("invalid year and week")
            
        #format_check_yw = year_week.split("-")
        current_year = date.today().year()
        
        formatweek = year_week [4:6]
        formatyear = year_week [0:3]
        int(formatweek)
        
        if formatweek < 1 or int(formatweek) > 52 and int(formatyear) > current_year:
            print("invalid year and week given please enter in the correct format")
       
    
#-------------------------------------------------------------------------------------------
    while True:
        try:
            number_of_vegan = float(input("Enter number of vegan hotdogs in format "))
            
        except ValueError:
            
            print("invalid number of vegan hotdogs entered")    
      #-----------------------------

    while True:
        try:
            number_of_meat_hotdogs = float(input("Enter number of meatdogs in format "))
        except ValueError:
            print("invalid number of meat hotgos entered ")    
      
#----------------------------------------------------------------------------
    onions = float(input("Enter Kg of onions "))
    
#-------------------------------------------------------------------------------    
    while True:
        try:
            ketchup = int(input("Enter ketchup in litres "))
        except ValueError:
            print("invalid amount of ketchup entered") 
    
#------------------------------------------------------------------------
    
    
    new_vendor = [
        
        vendor_id,
        vendor_name,
        number_of_vegan,
        number_of_meat_hotdogs,
        onions,
        ketchup
        
        ]
    
    print("you have entered")
    print(new_vendor)
#----------------------------------------------------------------------------------------    
    user_confirmation = input("are you happy with this information")
    if user_confirmation.lower() == "yes" :
        safe_data = data.copy
        data.append(new_vendor)
        with open("Hotdogs (1).txt" ,"a")as file:
            file.write(new_vendor)
        print("Vendor added")

    else:
        print("vendor not saved")

#add_vendor(hotdog_data)




#quick sort
def quick sort(data):
    pivot = data[0]
    left[]
    right[]
    for item in data
    [0] < pivot 
#-----------------------------------------------------------------------------------------------------------













import datetime  #built in module for handling dates and times 
import sys


def read_data(filename): #read vendor data from text file and store them
    
    data = [] # dataset
    
    try:

        with open(filename, "r") as file: #with statement makes sure file is closed after use
            lines = file.readlines() #The readlines() method returns a list containing each line in the file as a list item.

    except FileNotFoundError:
         print(" Error: File not found")

        
    for item in lines:
            columns = item.strip().split(",")
            
        
            row = [
                
                columns[0], #vendor ID
                columns[1], #Vendor name 
                columns[2], # year and week 
                int(columns[3]), #number of vegan hotdogs 
                int(columns[4]), # Number of meat hotdogs 
                float(columns[5]), # Onions(Kg)
                float(columns[6]), # Ketchup (litres)
                

                     ]
            data.append(row)

                 
    return data
    

hotdog_data = read_data("Hotdogs (1).txt")
#-----------------------------------------------------------------------------------------------------------------------------
def linear_search_unsorted(data):
    target = input("Search Vendors")
    
    for row in hotdog_data:
        if row[1].lower() == target.lower():
         
           
            print("Vendor ID:", row[0])
            print("Vendor name:", row[1])
            print("Year and Week:", row[2])
            print("Number of vegan hotdogs:", row[3])
            print("Number of meat hotdogs:", row[4])
            print("Onions (Kg):", row[5])
            print("Ketchup (Litres):", row[6])
            return       
    else:
        print("vendor not found")

               
#linear_search_unsorted(hotdog_data)

#-------------------------------------------------------------------------------------------------------------------
#linear search nyw (name year week)
def linear_search_unsorted_nyw(data):
    target_name = input("Search Vendors")
    target_yw = int(input("enter year week in format yyyywwww"))
    
    for row in hotdog_data:
        if row[1].lower() == target_name.lower() and int(row[2])== target_yw:
         
            import datetime
            print("Vendor ID:", row[0])
            print("Vendor name:", row[1])
            print("Year and Week:", row[2])
            print("Number of vegan hotdogs:", row[3])
            print("Number of meat hotdogs:", row[4])
            print("Onions (Kg):", row[5])
            print("Ketchup (Litres):", row[6])
            return
        

    print("vendor not found")


               
#linear_search_unsorted_nyw(hotdog_data)



def search_menu(data):
    print( "Option 1 search by vendor name")
    print("option 2 search by vendor name, year and week")

    choice = int(input("enter choice 1 or 2"))

    if choice == 1 :
        linear_search_unsorted(hotdog_data)

    elif choice == 2 :
        linear_search_unsorted_nyw(hotdog_data)
    else:
        print("invalid option")
#----------------------------------------------------------------------------------------------------        

#search_menu(hotdog_data)
#--------------------------------------------------------------------------------------------


        

def add_vendor(data):

    
    while True:
        
        vendor_id = input("Enter vendor id in the format - XX_DDD - ").upper()
        if len(vendor_id) == 6: 
            f_alpha_vendor_id = vendor_id [0:2]
            f_numb_vendor_id = vendor_id [4:6]
            f_u_vendor_id = vendor_id[3]
            
            if f_numb_vendor_id.isdigit() or f_alpha_vendor_id.isalpha() or f_u_vendor_id == "_" :
                print("")
                break
            else:
                print("formatting error please ensure it's two letters an underscore and 3 numbers")
        else:
                print("length error: id must be 6 characters ;long")


    
    
#-----------------------------------------------------------------------------
    #validation
    
    while True:
        name_valid = True
        vendor_name = input("Enter vendor name in format")

        try:
            if not vendor_name or not all(c.isalpha() or c.isspace() for c in vendor_name):
                raise ValueError

            if len(vendor_name) < 2 or len(vendor_name) > 25:
                print("Invalid vendor name")
                name_valid = False
                
        except ValueError:
            print("invalid vendor name")
            name_valid = False
        if name_valid :
            break
       
            
        
# -----------------------------------------------------------------------------------------
    while True:
        year_week = int(input("Year and week of info in format [ YYYYWW ] "))
        if len(str(year_week)) == 6 :

            now = datetime.datetime.now() # variable captures the exact year month day hour minute and second code runs 
            current_year = now.strftime("y%")
            int(current_year)
            int(current_week)
            current_week = now.strftime("%w")
        
            formatweek = year_week [4:6]
            formatyear = year_week [0:3]
            
        
            if not formatweek < 1 or formatweek > 52 and formatyear > current_year and formatweek > current_week :
                print("")
                break
            else:
                print("invalid year and week entered")
                
        else:
            print("length error please enter the year then the week with no spaces in between")    
       
    
#-------------------------------------------------------------------------------------------
    while True:
        try:
            number_of_vegan = float(input("Enter number of vegan hotdogs in format "))
            
        except ValueError:
            
            print("invalid number of vegan hotdogs entered")    
      #-----------------------------

    while True:
        try:
            number_of_meat_hotdogs = float(input("Enter number of meatdogs in format "))
        except ValueError:
            print("invalid number of meat hotgos entered ")    
      
#----------------------------------------------------------------------------
    onions = float(input("Enter Kg of onions "))
    
#-------------------------------------------------------------------------------    
    while True:
        try:
            ketchup = int(input("Enter ketchup in litres "))
        except ValueError:
            print("invalid amount of ketchup entered") 
    
#------------------------------------------------------------------------
    
    
    new_vendor = [
        
        vendor_id,
        vendor_name,
        number_of_vegan,
        number_of_meat_hotdogs,
        onions,
        ketchup
        
        ]
    
    print("you have entered")
    print(new_vendor)
#----------------------------------------------------------------------------------------    
    user_confirmation = input("are you happy with this information")
    if user_confirmation.lower() == "yes" :
        safe_data = data.copy
        data.append(new_vendor)
        with open("Hotdogs (1).txt" ,"a")as file:
            file.write(new_vendor)
        print("Vendor added")

    else:
        print("vendor not saved")

add_vendor(hotdog_data)

