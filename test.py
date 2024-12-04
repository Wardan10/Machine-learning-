import csv,collections
data = [
    ["ID1", "Minneapolis", "shoes", 2, "Air"],
    ["ID2", "Chicago", "shoes", 1, "Air"],
    ["ID3", "Central Department Store", "shoes", 5, "BonPied"],
    ["ID4", "Quail Hollow", "forks", 3, "Pfitzcraft"]
]
test=collections.defaultdict()
for all in data:
    test[all[2]][all[4]]+=all[3]
for i,j in test.items():
    print(i,j)
# with open("test1.csv",mode='w',newline="") as file:
#     writer=csv.writer(file)
#     for keys,values in test.items():
#         writer.writerow({keys,values})
