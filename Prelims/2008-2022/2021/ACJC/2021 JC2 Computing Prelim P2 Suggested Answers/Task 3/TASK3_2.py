# TASK 3.2
import pymongo

# Set up client and connect to the database
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("community_centre")
coll = db.get_collection("management_committee") 

# Clear the collection if it already exists
if coll.find().count != 0:
    coll.delete_many({})

# Open file and process each line
with open("VACCINATION.txt") as f1:
    for line in f1:
        lst = line.strip().split(",") 
        mem_id, name = int(lst[0]), lst[1] # Handle member ID and name
        first, second = "N/A", "N/A"
        remarks = None

        # Handle remarks
        if not lst[-1].isdigit() and len(lst) > 2:
            remarks = lst[-1]
            lst.pop()

        # Handle date of first and second dose
        if len(lst) == 3:   # Taken only the first dose
            first = lst[2]
        elif len(lst) == 4: # Taken both the first and second doses
            first = lst[2]
            second = lst[3]

        # Insert documents accordingly
        if remarks:
            coll.insert_one({"_id":mem_id,
                             "name":name,
                             "date_first_dose":first,
                             "date_second_dose":second,
                             "remarks":remarks}) 
        else:
            coll.insert_one({"_id":mem_id,
                             "name":name,
                             "date_first_dose":first,
                             "date_second_dose":second})

# Close the client
client.close()
