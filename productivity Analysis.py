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

#-----------------------------------------------------


def quick_sort(data): #sort by vendor and year and week
    if len(data) <= 1:
        return data
    pivot = data[len(data)//2] #find median row
    pivot_n = pivot[1].lower() #vendor name within that row
    pivot_yw = int(pivot[2])   #year and week from that row 
    

    left =[]
    middle = []
    right = []
    
    for row in data: #for every list within data 
        vendor = row[1].lower() #vendor name is index one of the list
        yearweek = int(row[2])  #year and week are in index two of the list 
        
        if vendor < pivot_n :   #if vendor name less than pivot value
            left.append(row)
            
        elif vendor > pivot_n:  #if vendor name is greater than pivot 
            right.append(row)

        else:

            if yearweek < pivot_yw:     #if year and week are less than the pivot 
               left.append(row)

            elif yearweek > pivot_yw:   #if year and week are greater than the pivot 
               right.append(row)
               
            else:
                middle.append(row)      #if the values are the same place them in the middle


    sorted_list = quick_sort(left)+ middle + quick_sort(right) #sort all the values in the sub lists then join them
    return sorted_list

#------------------------------------
#quick_sort(hotdog_data)
#---------------------------------------


#quick_sorted_data = quick_sort(hotdog_data)
    
#view_file_qs = input("Do you want to see the sorted file yes/no?: ")
    
#if view_file_qs.lower()== "yes": #allow user option to see sorted file if they wish 
    
    #for row in quick_sorted_data:
        #print(row)
        #print("") #?
   # print("File sorted")
#else:
    #print("File sorted")

#----------------------------------------


def vendor_analysis(data):
    productive_vendor = data[0]
    best_score = (data[0][3] + data[0][4]) / data[0][6]


    for row in data:
        meat_h = row[3]
        vegan_h = row[4]
        ketchup = row[6]

        curr_score = (meat_h + vegan_h) / ketchup
        

        if curr_score > best_score:
            best_score = curr_score
            productive_vendor = row

            
        print("Vendor ID:", productive_vendor[0])
        print("Vendor name:",productive_vendor [1])
        print("Year and Week:",productive_vendor [2])
        print("Number of vegan hotdogs:", productive_vendor[3])
        print("Number of meat hotdogs:",productive_vendor [4])
        print("Onions (Kg):", productive_vendor[5])
        print("Ketchup (Litres):",productive_vendor[6]) 
        

        return productive_vendor

vendor_analysis(hotdog_data)
