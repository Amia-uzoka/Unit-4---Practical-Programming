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

