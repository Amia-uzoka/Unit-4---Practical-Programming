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
# for row in hotdog_data:
# print(row)
# -------------------------------------------------------------

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
                "Enter vendor ID Ensure its in the format XX_YYY  (two letters an underscore followed by 3 numbers) "
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
                "Hotdogs.txt", "a",encoding="utf8"
            ) as file:  # appends data to text file without overwriting existing file

                file.write(f"{n_l}\n")
                print("Vendor added")

        else:
            print("vendor not saved")


add_vendor(hotdog_data)

for row in hotdog_data:
    print(row)
