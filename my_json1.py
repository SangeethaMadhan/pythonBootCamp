import json # Open dictionary

f = open("default.json") # Open json file
file = json.load(f) # Converting json to python

for country in file: # For adding back to supportedSide first loop country key and then document key
    if country[0] == 'a':

        for document in file[country]:
            file[country][document]['supportedSide'].append("back") # Adding back along with front in supportedSide using append()

print(file['gtm'])

file["sww"] = file ["alb"]
print (file)

addedFile = open("sww_addedFile",'w')
addedFile.write(json.dumps(file, indent = 4))
