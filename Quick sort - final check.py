"""read vendor data from text file and store them"""


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


# for row in hotdog_data:
# print(row)
# --------------------------------------------
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


display_vendors_qs()
