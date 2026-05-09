

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

#-----------------------------------------------
# vendor_analysis(hotdog_data)
# ----------------------------------------------
#------------------------------------------------------------------------

import json  # module needed to access the json.dump(x,f,indent)


def save_analysis(filename):

    analysis_results = vendor_analysis(hotdog_data)

    with open(filename, "w", encoding="utf8") as file:
        json.dump(
            analysis_results, file, indent=4
        )  # converts dictionary into a file format

    print(f"Results succesfully saved to: {filename}")


save_analysis("AnalysisOutput.txt")
