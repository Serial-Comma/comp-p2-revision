# TASK 3.3
import pymongo

# Set up client and connect to the database
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("community_centre")
coll = db.get_collection("management_committee")

# From Task 1.1
def second_dose_date(date):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = int(date[4:6])
    day = int(date[6:])

    new_month = month + ((day + 21) // days[month-1])
    new_day = (day + 21) % days[month-1]
    
    if new_month < 10:
        new_month = "0" + str(new_month)
    else:
        new_month = str(new_month)

    if new_day < 10:
        new_day = "0" + str(new_day)
    else:
        new_day = str(new_day)

    result = "2021" + new_month + new_day
    
    return result

user = ""

# Prompt with validation
while not user.isdigit():
    user = input("Input member ID: ")

# Query to retrieve the document given the member ID
doc = coll.find_one({"_id":int(user)})

# If member ID can be found
if doc:
    # Extract name and dates of first and second dose, if any
    name = doc["name"]
    date1 = doc["date_first_dose"]
    date2 = doc["date_second_dose"]

    # No first dose
    if date1 == "N/A":
        print("The member has not taken the first dose yet.")
        print("He/she should book for an appointment as soon as possible.")

    # No second dose
    elif date2 == "N/A":
        print("Date of second dose:", second_dose_date(date1))

    # Both doses taken
    else:
        # Open the text file in write mode (HIGHLIGHT ABOUT CLOSING!!!)
        with open("TASK3_3_your name_centre number_index number.txt", 'w') as f1:
            f1.write("VACCINATION CERTIFICATE\n\n")
            f1.write("Name: " + name + "\n")
            f1.write("Vaccine type: CoviDie\n")
            f1.write("Date of first dose: " + date1 + "\n")
            f1.write("Date of second dose: " + date2)

        # Update document with download indicator
        coll.update_one({"_id":int(user)},
                        {"$set":{"download":True}})

# If member ID cannot be found
else:
    print("The member ID entered is not present in the database.")

# Close the client
client.close()
