import sqlite3

# Connect to the database
connection = sqlite3.connect("bento_company.db")

kiosk_lst = []
bento_lst = []
markup = [2.60, 2.90, 2.40, 3.10] # Sell price = production cost + markup

# Open and process each line in the text file
# Insert records into Kiosk table 
with open("KIOSK.txt") as f1:
    for line in f1:
        lst = line.strip().split(",")
        kiosk_lst.append(int(lst[0])) # Extract only the KioskID to kiosk_lst
        connection.execute("INSERT INTO Kiosk VALUES (?, ?, ?)",
                           (int(lst[0]), lst[1], float(lst[2])))

# Insert records into BentoBox table
with open("BENTOBOX.txt") as f2:
    for line in f2:
        lst = line.strip().split(",")
        bento_lst.append([lst[0], float(lst[1])]) # Extract only the bento name and price to bento_lst
        connection.execute("INSERT INTO BentoBox VALUES (?, ?, ?, ?, ?)",
                           (lst[0], float(lst[1]), int(lst[2]), int(lst[3]), int(lst[4])))

# Insert records into KioskBento table
for i in range(len(kiosk_lst)):
    kiosk = kiosk_lst[i]
    for j in range(len(bento_lst)):
        bento = bento_lst[j][0]
        price = float(bento_lst[j][1]) + markup[i] # Calculate sell price
        connection.execute("INSERT INTO KioskBento VALUES (?, ?, ?)",
                           (kiosk, bento, price))

# Commit changes and close the connection
connection.commit()
connection.close()
