import json
import glob, os


os.chdir("data_bags/users")
for file in glob.glob("*.json"):
  # print(file)
  # Opening JSON file
  f = open(file)
  
  # returns JSON object as 
  # a dictionary
  data = json.load(f)

  if 'users' in data['groups']:
    print (data['id'])
    # print (data['groups'])
  
  f.close()

