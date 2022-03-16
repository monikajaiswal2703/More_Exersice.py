import json
with open("users.json","r") as json_file:
    data=json.load(json_file)
for i in data:
    for j in data[i]:
        print ("users full name is ",  j['firstName'] , j['lastName'])
        print ("users mobile number is ",  j['details']['mobileNo'])
        print ("users age  is " , j ['details']['age'])
        print ("users city is ", j['details']['City'])





