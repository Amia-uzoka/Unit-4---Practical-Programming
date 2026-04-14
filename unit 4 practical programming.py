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

