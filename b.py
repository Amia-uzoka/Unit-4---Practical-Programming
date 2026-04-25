from datetime import date

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
        today = date.today()
        current_year = today.strftime("%Y")
        int(current_year)
        year= int(input("Enter year:"))
        week = int(input("enter week:"))
        if not week < 1 or week > 52 :
            print("invalid  week")
            if not year > current_year :
                print("invalid year inputed")    
       
    
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
#------------------------------------------------------------

import math
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

            
 
    
        
    return data
    

hotdog_data = read_data("Hotdogs (3).txt")


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

        try:
            year= int(input("Enter year:"))
            week = int(input("enter week:"))
            
            if year > 2026:
                print("invalid year")
            elif week < 1 or week > 52:
              print("invalid week")
            
            else:
                vendor_date = str(year)+ str(week).zfill(2)
                break
        except ValueError:
            print("numbers only")
                
                
            
            
         
       
    
#-------------------------------------------------------------------------------------------
    while True:
        try:
            number_of_vegan = float(input("Enter number of vegan hotdogs in format "))
            break
        except ValueError:
            print("invalid number of vegan hotdogs entered")    
      #-----------------------------

    while True:
        try:
            number_of_meat_hotdogs = float(input("Enter number of meatdogs in format "))
            break
        except ValueError:
            print("invalid number of meat hotgos entered ")    
      
#----------------------------------------------------------------------------
    while True:
        try:
            onions = float(input("Enter Kg of onions "))
            if onions - math.trunc(onions) == 0.5 or onions - math.trunc(onions)== 0:
                print("")
                break
            else:
                print("the weight of the onions must be in half kilogram increments (e.g o.5 or 0.0")
        except ValueError:
            print("numbers only")
            
    
    


    
    
#-------------------------------------------------------------------------------    
    while True:
        try:
            ketchup = int(input("Enter ketchup in litres "))
            if ketchup < 1 or ketchup > 4 :
                print("must be between 1 and 4 litres")
            else:
                print("")
                break
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

def quick_sort(data): #sort by vendor and year and week
    if len(data) <= 1:
        return data
    pivot = data[len(data)//2] # find median row
    pivot_n = pivot[1].lower() #vendor name 
    pivot_yw = int(pivot[2])# year week
    

    left =[]
    middle = []
    right = []
    
    for row in data:
        vendor = row[1].lower()
        yearweek = int(row[2])
        
        if vendor < pivot_n :
            left.append(row)
            
        elif vendor > pivot_n:
            right.append(row)

        else:

            if yearweek < pivot_yw:
               left.append(row)

            elif yearweek > pivot_yw:
               right.append(row)
               
            else:
                middle.append(row)
        
  
    return quick_sort(left)+ middle + quick_sort(right)
    
quick_sorted_data = quick_sort(hotdog_data)
user_input_view_sorted_filee = input("Do you want to see the sorted file yes/no?: ")
if user_input_view_sorted_filee.lower()== "yes": #allow user option to see sorted file if they wish 
    for row in quick_sorted_data:
        print(row)
else:
    exit  

    
