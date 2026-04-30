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
    

hotdog_data = read_data("Hotdogs (24).txt")
        
 
#------------------------------------------------------------------


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

#---------------------------------------------------------------

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

  
    return quick_sort(left)+ middle + quick_sort(right) #sort all the values in the sub lists then join them 
    


#-----------------------------------------------------------------

import time
start_time = time.perf_counter()

quick_sort(hotdog_data)

#bubble_sort(hotdog_data)

end_time = time.perf_counter()

time_passed = end_time - start_time

print(f"Quick sort took: {time_passed:.6f} seconds")
