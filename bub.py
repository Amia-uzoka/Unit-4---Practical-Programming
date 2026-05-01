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
                float(columns[6]), # Ketchup (litres)
                

                     ]
            data.append(row)
        
    except FileNotFoundError:
         print("File not found")
             
        
    return data
hotdog_data = read_data("Hotdogs(130).txt")
#--------------------------------------------------------------------------
def bubble_sort(data):
    new_data = data.copy() 
    n = len(new_data)
    
    for i in range(n):
        swapped = False  # Reset for each pass through the list
        
        # Optimization: len - 1 - i because the last i elements are already sorted
        for j in range(n - 1 - i):

            #if the name on the left is further down the alphabet than on the right swap
            if new_data[j][1].lower() > new_data[j+1][1].lower():
                new_data[j], new_data[j + 1] = new_data[j + 1], new_data[j]
                swapped = True 
        
        # If no two elements were swapped in the inner loop, the list is sorted
        if not swapped:
            break
    print("file sorted")        
    return new_data


bubble_sort(hotdog_data)

bubble_sorted_data = bubble_sort(hotdog_data)
    
view_file_bs = input("Do you want to see the sorted file yes/no?: ")
    
if view_file_bs.lower()== "yes": #allow user option to see sorted file if they wish 
    
    for row in bubble_sorted_data:
        print(row)
        print("") #?
    print("File sorted")
else:
    print("File sorted")

