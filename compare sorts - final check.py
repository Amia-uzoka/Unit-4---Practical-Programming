"""read vendor data from text file and store them"""


def read_data(filename):

    data = []  # dataset
    try:

        with open(
            filename, "r", encoding="utf8"
        ) as file:  # with statement makes sure file is closed after use
            lines = file.readlines()  # The readlines() method returns a list
            # containing each line in the file as a list item.

        for item in lines:
            columns = item.strip().split(",")

            # takes each list one at a time and splits the big string into a list of substrings
            # using [,] as the seperator
            # split removes trailing snd leading whitespace

            current_row = [
                columns[0],  # vendor ID
                columns[1],  # Vendor name
                columns[2],  # year and week
                int(float((columns[3]))),  # number of vegan hotdogs
                int(float(columns[4])),  # Number of meat hotdogs
                float(columns[5]),  # Onions(Kg)
                int(columns[6]),  # Ketchup (litres)
            ]
            data.append(current_row)

    except FileNotFoundError:
        print("File not found")

    return data


hotdog_data = read_data("Hotdogs.txt")

# ------------------------------------------------------------------

def bubble_sort(data):
    new_data = data.copy()
    n = len(new_data)

    for i in range(n):
        swapped = False  # Reset for each pass through the list

        # Optimization: len - 1 - i because the last i elements are already sorted
        for j in range(n - 1 - i):

            # if the name on the left is further down the alphabet than on the right swap
            if new_data[j][1].lower() > new_data[j + 1][1].lower():
                new_data[j], new_data[j + 1] = new_data[j + 1], new_data[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the list is sorted
        if not swapped:
            break

    return new_data

# -----------------------------------------------------------------
def quick_sort(data):  # sort by vendor and year and week
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]  # find median row
    pivot_n = pivot[1].lower()  # vendor name
    pivot_yw = int(pivot[2])  # year week

    left = []
    middle = []
    right = []

    for row in data:
        vendor = row[1].lower()
        yearweek = int(row[2])

        if vendor < pivot_n:  # check if vendor name is smaller than pivot
            left.append(row)

        elif vendor > pivot_n:  # check if vendor name is greater than pivot
            right.append(row)

        else:

            if yearweek < pivot_yw:  # check if the year and week is smaller than pivot
                left.append(row)

            elif (
                yearweek > pivot_yw
            ):  # check if the year and week is greater than pivot
                right.append(row)

            else:
                middle.append(
                    row
                )  # if items are equivalent to pivot place in the middle

    return quick_sort(left) + middle + quick_sort(right)

#------------------------------------------------------------------
import time

start_time = time.perf_counter()

# quick_sort(hotdog_data)

# bubble_sort(hotdog_data)

end_time = time.perf_counter()

time_passed = end_time - start_time

print(f"Bubble sort / Quick sort took: {time_passed:.6f} seconds")
