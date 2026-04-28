import math
import string
import sys

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

#------------------------------------------------------------------



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
    
quick_sort(hotdog_data)
quick_sorted_data = quick_sort(hotdog_data)
    
view_file_qs = input("Do you want to see the sorted file yes/no?: ")
    
if view_file_qs.lower()== "yes": #allow user option to see sorted file if they wish 
    
    for row in quick_sorted_data:
        print(row)
        print("") #?
    print("File sorted")
else:
    print("File sorted")
#--------------------------------------------------



def binary_search(data):
    
    quick_sort(hotdog_data)
    
    target_vendor =input("Searcch vendors")
    target_yw = input("enter year and week")

    low = 0
    high = len(data) - 1

    while low <= high:
        midpoint = (low + high) // 2
        row = data[midpoint] #row at midpoint
        mid_name = row[1].lower()
        mid_yw = row[2]

        if mid_name == target_vendor and mid_yw == target_yw:
             
            print("Vendor ID:", row[0])
            print("Vendor name:", row[1])
            print("Year and Week:", row[2])
            print("Number of vegan hotdogs:", row[3])
            print("Number of meat hotdogs:", row[4])
            print("Onions (Kg):", row[5])
            print("Ketchup (Litres):", row[6])
            return
                
            return row
        
        if  ( mid_name < target_vendor ) or ( mid_yw < target_yw ):
            low = midpoint + 1
            
        else:
            high = midpoint - 1
    print("Vendor not found" )
    return None

binary_search(hotdog_data)

            
         
    
