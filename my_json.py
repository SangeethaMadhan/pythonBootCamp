import json # Open dictionary

f = open("default.json") # Open json file
file = json.load(f) # Converting json to python
x = file.keys()
y = print("No. of countries: ", len(x))

print(x)

total_count = 0
for i in file:
    keys = list(file[i].keys())
    print(keys)
    count = len(keys)
    total_count = total_count + count
print("Total number of documents: ", total_count)
