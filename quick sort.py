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
