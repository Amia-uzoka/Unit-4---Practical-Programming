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


# for row in hotdog_data:
# print(row)
# ----------------------------------------------------------------------------


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


quick_sorted_data = quick_sort(hotdog_data)


# ----------------------------------------------------------


def linear_search_sorted_nyw(data):

    try:

        found = False
        target_name = input("Search vendors: ")
        target_yw = int(input("Enter year(Y) and week(W) in the format YYYYWW: "))

        for row in hotdog_data:
            if row[1].lower() == target_name.lower() and int(row[2]) == target_yw:

                # check index 1 in every list(vendors names) and index the 2 (year & week)
                # if they are equal to the users target
                # print the vendors information

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
            print("vendor not found")

    except ValueError:
        print("Year and week must be numeric characters ")


# --------------------------------------------------------------------------------
def binary_search(data):

    target_vendor = input("Search vendors: ")
    target_yw = input("Enter year(Y) and week(W) in the form YYYYWW: ")

    low = 0
    high = len(data) - 1

    while low <= high:
        midpoint = (low + high) // 2
        row = data[midpoint]  # row at midpoint
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

            return row

        if (mid_name < target_vendor) or (mid_yw < target_yw):
            low = midpoint + 1

        else:
            high = midpoint - 1
    print("Vendor not found")
    return None


# -------------------------------------------------------------------------------------

import time

start_time = time.perf_counter()

#linear_search_sorted_nyw(quick_sorted_data)

binary_search(quick_sorted_data)


end_time = time.perf_counter()

time_passed = end_time - start_time

print(f"Binary search (on sorted data) took: {time_passed:.6f} seconds")
