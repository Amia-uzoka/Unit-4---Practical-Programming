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
