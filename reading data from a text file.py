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


#------------------------------------------------------------------------------------------------
def read_data(filename): #read vendor data from text file and store them
    
    data = [] # dataset
    try:

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
        
    except FileNotFoundError:
         print("File not found")
             
        
    return data
hotdog_data = read_data("Hotdogs (1).txt")
for row in hotdog_data:
    print(row)

#----------------------------------------------------------------------------------------------------------

#Finished product
def read_data(filename): #read vendor data from text file and store them
    
    data = [] # dataset
    try:

        with open(filename, "r") as file: #with statement makes sure file is closed after use
            lines = file.readlines() #The readlines() method returns a list containing each line in the file as a list item.

        
        for item in lines:
            columns = item.strip().split(",")
            
        # takes each list one at a time and splits the big string into a list of substrings using [,] as the seperator  
        # split removes trailing snd leading whitespace
        
            row = [
                
                columns[0], #vendor ID
                columns[1], #Vendor name 
                columns[2], # year and week 
                int(float((columns[3]))), #number of vegan hotdogs 
                int(float(columns[4])), # Number of meat hotdogs 
                float(columns[5]), # Onions(Kg)
                int(columns[6]), # Ketchup (litres)
                

                     ]
            data.append(row)
        
    except FileNotFoundError:
         print("File not found")
             
        
    return data
hotdog_data = read_data("Hotdogs(130).txt")
