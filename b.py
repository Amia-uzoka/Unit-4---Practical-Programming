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


    
