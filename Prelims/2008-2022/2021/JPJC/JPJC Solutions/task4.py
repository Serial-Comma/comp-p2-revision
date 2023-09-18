#Task 4.1
import pymongo, json
client = pymongo.MongoClient("127.0.0.1", 27017)

db = client.get_database("jp_mobile")
coll = db.get_collection("phone")
x = coll.delete_many({})
print(x.deleted_count, " documents deleted.")

with open('item.json') as file:
    data = json.load(file)
coll.insert_many(data)

#Task 4.2
brand = input("Enter brand: ")
model = input("Enter model: ")
color = input("Enter colour: ")
price = int(input("Enter price: "))
qty   = int(input("Enter quantity: "))
gift = []
while True:
    free = input("Enter free gift [NA if not applicable]: ")
    if free.upper() != "NA":
        gift.append(free)
    else:
        break
#search for existing phone model
result = coll.find()
for doc in result:
    if brand == doc.get('brand') and model == doc.get('model') and color == doc.get('colour'):
        qty = qty + doc.get('quantity')
coll.delete_one({"brand":brand,"model":model,"colour":color})
coll.insert_one({"brand":brand,"model":model,"colour":color,\
                 "price":price,"quantity":qty,"free_gift":gift})

##value = 'solo'
##rows=[]
##for doc in result:
##    if doc.get('brand') == value:
##                rows.append((doc.get('price'),doc.get('model'),doc.get('colour')))        

#Task 4.3
def display_all():
    result = coll.find()
    print("All documents in phone collection:")
    print("{:<15}{:<10}{:<10}{:<6}{:<10}{:<20}".\
          format("brand","model","colour","price","quantity","free gifts"))
    for document in result:
        print("{:<15}{:<10}{:<10}{:<6}{:<10}{:<20}".format(document.get('brand'), \
                                                    document.get('model'), \
                                                    document.get('colour'), \
                                                    document.get('price'), \
                                                    document.get("quantity"), \
                                                    str(document.get("free_gift"))))
    print("Number of documents:", coll.count())

display_all()
client.close()
