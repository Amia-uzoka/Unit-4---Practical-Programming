import math
import string
import sys


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


for row in hotdog_data:
    print(row)

print("\n")


# -------------------------------------------------------- linear search unsorted


def linear_search_unsorted_nyw(data):

    try:

        found = False
        target_name = input("Search vendors: ")
        target_yw = int(input("Enter year(Y) and week(W) in the format YYYYWW: "))

        for row in hotdog_data:
            if row[1].lower() == target_name.lower() and int(row[2]) == target_yw:

                # check index 1 in every list(vendors names) and index the 2 (year & week) if they are equal to the users target
                # print the vendors information

                print("\n")
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


# ----------------------------------------
linear_search_unsorted_nyw(hotdog_data)
# ----------------------------------------

print("Searched vendors via linear search algorithim (on unsorted data)")
print("\n")


# -----------------------------------------------------  quick sort


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


# If you want to see the sorted file


def display_vendors_qs():
    quick_sorted_data = quick_sort(hotdog_data)
    print("File Sorted")
    user_input_view_sorted_filee = input("Do you want to see the sorted file yes/no?: ")
    if (
        user_input_view_sorted_filee.lower() == "yes"
    ):  # allow user option to see sorted file if they wish
        for row in quick_sorted_data:
            print(row)
    else:
        sys.exit()


# ----------------------------------------
display_vendors_qs()
# ---------------------------------------
print("Successfully sorted file via quick sorting algorithim")
print("\n")

# --------------------------------------------------------------  linear search sorted


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

                print("\n")
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


# --------------------------------------------
linear_search_sorted_nyw(quick_sorted_data)
# --------------------------------------------


print("Searched vendors via linear searching algorithim (on sorted data)")
print("\n")


# ----------------------------------------------- binary search
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

            print("\n")
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


# -----------------------------
binary_search(quick_sorted_data)
# -------------------------------

print("Searched vendors via binary searching algorithim ")
print("\n")


# ---------------------------------------------------------------bubble sort
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


def display_vendors_bs():
    """Display the list of vendors to the user"""
    bubble_sorted_data = bubble_sort(hotdog_data)
    print("File Sorted")
    user_input_view_sorted_filee = input("Do you want to see the sorted file yes/no?: ")
    if (
        user_input_view_sorted_filee.lower() == "yes"
    ):  # allow user option to see sorted file if they wish

        for row in bubble_sorted_data:
            print(row)
    else:
        sys.exit()


# -------------------------------
display_vendors_bs()
# --------------------------------

print("Successfully sorted file via bubble sorting algorithim")
print("\n")
# ------------------------------------------- add vendor
PASSCODE = 1082421

"""Allow user to add vendors to the file"""


def add_vendor(data):

    user_password = int(input("Please enter password in order to continue "))
    if user_password != PASSCODE:
        print("You are not authorised to use this feature")
        sys.exit()

    elif user_password == PASSCODE:
        print("Passcode approved")

        # -------------------------------------------------------------------------------

        while True:

            # validation ensuring vendor ID is in the correct format

            vendor_id = input(
                "Enter vendor ID Ensure its in the format XX_YYY (two letters an underscore followed by 3 numbers) "
            ).upper()

            try:
                if len(vendor_id) == 6:
                    f_alpha_vendor_id = vendor_id[0:2]
                    f_numb_vendor_id = vendor_id[3:6]
                    f_u_vendor_id = vendor_id[2]

                    if (
                        f_numb_vendor_id.isdigit()
                        and f_alpha_vendor_id.isalpha()
                        and f_u_vendor_id == "_"
                    ):
                        print("Valid vendor ID ")
                        vendor_id.upper()
                        break
                    else:
                        print("Invalid vendor ID")
                        print("Please try again")
                else:
                    print("Invalid vendor ID")
                    print("Please try again")

            except ValueError:
                print("Invalid vendor ID")

        # -----------------------------------------------------------------------------

        while True:

            # validation ensuring vendor name is the appropriate length
            # and contains no unesscary characters

            name_valid = True
            vendor_n = input("Enter vendor name: ")

            try:
                if not vendor_n or not all(
                    c.isalpha() or c.isspace() for c in vendor_n
                ):
                    raise ValueError

                if len(vendor_n) < 2 or len(vendor_n) > 25:
                    print("Invalid vendor name")
                    print("Please try again")
                    name_valid = False

            except ValueError:
                print("Invalid vendor name")
                print("Please try again")
                name_valid = False

            if name_valid:
                vendor_name = string.capwords(vendor_n)
                print("Valid vendor name")
                break

        # -----------------------------------------------------------------------------------------

        while True:

            # validation ensuring year inputted is not greater than the current year
            # and week is within appropriate range

            try:
                year = int(input("Enter year:"))
                week = int(input("Enter week:"))

                if year > 2026:
                    print("Invalid year given")
                    print("Please try again")
                elif week < 1 or week > 52:
                    print("Invalid week")
                    print("Please try again")
                else:
                    vendor_date = str(year) + str(week).zfill(
                        2
                    )  # join values of year and week ( zfill() adds zero to the beginning of the string untol it reaches a length of 2
                    print("Valid date given")
                    break

            except ValueError:
                print("numbers only")

        # ------------------------------------------------------------------------------

        while True:
            try:
                number_of_vegan = int(input("Enter number of vegan hotdogs: "))
                print("Valid Input")
                break
            except ValueError:
                print("Invalid number of vegan hotdogs entered ")

        # --------------------------------------------------------------------------

        while True:
            try:
                number_of_meat_hotdogs = int(
                    input("Enter number of meatdogs in format ")
                )
                print("Valid Input")
                break
            except ValueError:
                print("Invalid number of meat hotdogs entered ")

        # ----------------------------------------------------------------------------

        while True:
            try:
                onions = float(input("Enter Kg of onions: "))
                if (
                    onions - math.trunc(onions) == 0.5
                    or onions - math.trunc(onions) == 0
                ):
                    print("Valid Input")
                    break
                else:
                    print(
                        "The weight of the onions must be in half kilogram increments (e.g 0.5 or 0.0"
                    )
            except ValueError:
                print("Invalid input numbers only ")

        # -------------------------------------------------------------------------------

        while True:

            # validation - ensuring user enters an amount within specified range

            try:
                ketchup = int(input("Enter ketchup in litres "))
                if ketchup < 1 or ketchup > 4:
                    print("Amount must be between 1 and 4 litres")
                else:
                    print("Valid Input")
                    break
            except ValueError:
                print("Invalid amount of ketchup entered ")

        # ------------------------------------------------------------------------

        new_vendor = [
            vendor_id,
            vendor_name,
            vendor_date,
            number_of_vegan,
            number_of_meat_hotdogs,
            onions,
            ketchup,
        ]

        print("You have entered: ")
        print(new_vendor)

        # ----------------------------------------------------------------------------------------

        user_confirmation = input(
            "Are you sure this is the correct information for your vendor? "
        )
        if user_confirmation.lower() == "yes":

            data.append(new_vendor)
            n_l = ",".join(map(str, new_vendor))
            with open(
                "Hotdogs.txt", "a", encoding="utf8"
            ) as file:  # appends data to text file without overwriting existing file

                file.write(f"{n_l}\n")
                print("Vendor added")
                print("\n")

        else:
            print("vendor not saved")
            print("\n")


# -------------------------------------
add_vendor(hotdog_data)
# --------------------------------------

for row in hotdog_data:
    print(row)

print("\n")


# ---------------------------------------------------------------- productivity analysis
def vendor_analysis(data):
    productive_vendor = data[0]
    best_score = (data[0][3] + data[0][4]) / data[0][6]

    # Create a score for vendors -find total number of hotdogs sold divide by amount of
    # ketchup to find who sold the most while using the least amount of ketchup

    for row in data:
        meat_h = row[3]
        vegan_h = row[4]
        ketchup = row[6]

        curr_score = (meat_h + vegan_h) / ketchup

        if curr_score > best_score:
            best_score = curr_score
            productive_vendor = row  # vendor with the best score is the most productive

    results = {
        "The most productive vendor": productive_vendor[1],
        "In the year and week": productive_vendor[2],
        "Vendor ID": productive_vendor[0],
        "Sold number of vegan hotdogs": productive_vendor[3],
        "Sold number of meat hotdogs": productive_vendor[4],
        "For a total hotdog output of": productive_vendor[3] + productive_vendor[4],
        "Amount of Ketchup used (Litres)": productive_vendor[6],
    }

    for key, value in results.items():  # take all the keys in the dictionary
        print(f"{key} : {value}")

    print(
        "They were able to sell the most amount of hotdogs while using the least amount of ketchup"
    )
    return results


# ---------------------------
# vendor_analysis(hotdog_data)
# ----------------------------

# ---------------------------------------------------- save analysis to output file


import json  # module needed to access the json.dump(x,f,indent)


def save_analysis(filename):

    analysis_results = vendor_analysis(hotdog_data)

    with open(filename, "w", encoding="utf8") as file:
        json.dump(
            analysis_results, file, indent=4
        )  # converts dictionary into a file format

    print(f"Results succesfully saved to: {filename}")


# ----------------------------------------
save_analysis("AnalysisOutput.txt")
# -----------------------------------------
print("Succesfully analysed and saved results to an output file")
print("\n")

# -------------------------------------------------- compare the efficiency of the bubble sort
import time

start_time = time.perf_counter()

bubble_sort(hotdog_data)
display_vendors_bs()

end_time = time.perf_counter()

time_passed = end_time - start_time

print(f"Bubble sort took: {time_passed:.6f} seconds")
print("\n")

# -------------------------------------------------- compare the efficiency of the quick sort
import time

start_time = time.perf_counter()

quick_sort(hotdog_data)
display_vendors_qs()
end_time = time.perf_counter()

time_passed = end_time - start_time

print(f"Quick sort took: {time_passed:.6f} seconds")
print("\n")

# ---------------------------------------------------compare the efficiency of the binary search

import time

start_time = time.perf_counter()


binary_search(quick_sorted_data)

end_time = time.perf_counter()

time_passed = end_time - start_time

print(f"Binary search (on sorted data) took: {time_passed:.6f} seconds")
# --------------------------------------------------------------------------
print("\n")

# ---------------------------------------------------compare the efficiency of the linear search(sorted)

import time

start_time = time.perf_counter()

linear_search_sorted_nyw(quick_sorted_data)

end_time = time.perf_counter()

time_passed = end_time - start_time

print(f"Linear search (on sorted data) took: {time_passed:.6f} seconds")
# --------------------------------------------------------------------------
