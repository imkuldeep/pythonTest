#!C:/Users/kuldeepsingh/AppData/Local/Programs/Python/Python37-32/python3.exe
print("Content-Type: text/html")
print()

import json
import requests
import cgi
from haversine import haversine




sourceLat=53.339428
sourceLong=-6.257664
radiusDistance=100



form='''
<h2>Show Near users from source</h2>
<form method="POST" action="">
<label>Source Point: <label><br><br>
<label>Latitude</label>
<input type="text" name="latitude" placeholder="53.339428" value="%s"><br><br>
<label>Longitude</label>
<input type="text" name="longitude" placeholder="-6.257664" value="%s"><br><br>
<label>Radius : <label>
<input type="text" name="radius" value="%s" placeholder="100"><br><br>
<input type="submit" value="Show" />
</form>


'''

formData = cgi.FieldStorage()

if formData :
	sourceLat=float(formData['latitude'].value)
	sourceLong=float(formData['longitude'].value)
	radiusDistance= formData['radius'].value
	
inputSource= tuple([sourceLat,sourceLong])
print(form%(sourceLat,sourceLong,radiusDistance))


'''if isinstance(inputSource, tuple):
	
else :
	inputSource=tuple(inputSource)
'''
#Crate empty users list
users=[]
for line in open('users.json','r').readlines():
    users.append(json.loads(line))

#Sort User on the basis of user id
sortedUsers = sorted(users, key=lambda k: k['user_id'])

print("<h2>Input Users List in sorted user id Format :</h2>")
strTable = "<html><table cellpadding='10'border='2' cellspacing='2'><tr><th>Index</th><th>User Id</th><th>Name</th><th>Latitude</th><th>Longitude</th><th>Distance(Km)</th></tr>"
count=1
for user in sortedUsers:
	dist=haversine(inputSource,(float(user['latitude']),float(user['longitude'])))
	strRW = "<tr><td>"+str(count)+ "</td><td>"+str(user['user_id'])+ "</td><td>"+str(user['name'])+"</td><td>"+str(user['latitude'])+"</td><td>"+str(user['longitude'])+"</td><td>"+str("{0:.3f}".format(dist))+"</td></tr>"
	strTable = strTable+strRW
	count=count+1
strTable = strTable+"</table></html>"
print(strTable)


print("------------------------------------------------------------------"*2)
print("<h2>Filtered Users within {} km from Dublin area({}, {}) </h2> ".format(radiusDistance,sourceLat,sourceLong))

filterTable = "<html><table cellpadding='10'border='2' cellspacing='2'><tr><th>Index</th><th>User Id</th><th>Name</th><th>Latitude</th><th>Longitude</th><th>Distance(Km)</th></tr>"

#Counter
i=1
for user in sortedUsers:
	#if() < 30):
	dist=haversine(inputSource,(float(user['latitude']),float(user['longitude'])))
	if(dist <= float(radiusDistance)):
		filterRow = "<tr><td>"+str(i)+ "</td><td>"+str(user['user_id'])+ "</td><td>"+str(user['name'])+"</td><td>"+str(user['latitude'])+"</td><td>"+str(user['longitude'])+"</td><td>"+str("{0:.3f}".format(dist))+"</td></tr>"
		filterTable = filterTable+filterRow
		i=i+1
filterTable = filterTable+"</table></html>"
print(filterTable)