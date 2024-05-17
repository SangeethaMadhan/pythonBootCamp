import json # Open dictionary

f = open("default.json") # Open json file
file = json.load(f) # Converting json to python
sww = 0
file ["sww"] = file["alb"]
file_added = open("sww_added.txt", 'w')
file_added.write("sww")
json.dump("sww", file)
file.close()
