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
#-------------------------------------------------------------------------------------

#linear search nyw (name year week)


def linear_search_unsorted_nyw(data):


    try:
        
        found = False
        target_name = input("Search vendors")
        target_yw = int(input("Enter year(Y) and week(W) in the format YYYYWW: "))
        
        for row in hotdog_data:
            if row[1].lower() == target_name.lower() and int(row[2])== target_yw:
                
        #check index 1 in every list(vendors names) and index the 2 (year & week) if they are equal to the users target
        #print the vendors information    
                print(" ")
                print("Vendor ID:", row[0])
                print("Vendor name:", row[1])
                print("Year and Week:", row[2])
                print("Number of vegan hotdogs:", row[3])
                print("Number of meat hotdogs:", row[4])
                print("Onions (Kg):", row[5])
                print("Ketchup (Litres):", row[6])
                found = True
                return
                
        if not found:
              print(" ")  
              print("vendor not found")
          
    except ValueError:
                print("Year and week must be numeric characters ")
            

               
#linear_search_unsorted_nyw(hotdog_data)


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

               
linear_search_unsorted(hotdog_data)



