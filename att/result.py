#!C:/Users/kuldeepsingh/AppData/Local/Programs/Python/Python37-32/python3.exe
# -*- coding: UTF-8 -*-
# enable debugging
import cgitb
cgitb.enable()

print("Content-Type: text/html")
print()

#print("Content-Type: text/plain;charset=utf-8")

import urllib.request
import cgi
from datetime import datetime

year = '2019'
#date_time_row = datetime.strptime('1 Jul 2019 12:59', '%d %b %Y %H:%M')
#print(date_time_row)

def getDateTimeOnly(date_time):
	if date_time == 'Sun':
		return True
	else :
		return False

form = cgi.FieldStorage()

try:
	text = form["text"].value 
	text = text.split('\r\n')
	
	#text.replace(" ", "")
	text2 = filter(lambda x: len(x) > 15 , text)
	#text2.strip()
	data = []
	for r in text2:
		if r == 'Regularize Attendance' :
			continue
		dayDic = {'in':'','out':''};
		r = ''.join(r.split())
		#r.replace(" ", "")
		#r = '1Jul12:59'
		print('\n',r,sep='\n')
		
		if(r[1].isdigit()):
			dayDic['date'] 	= r[0:2]+' '+r[2:5]+' '+ year
			dayDic['in'] 	= r[0:2]+' '+r[2:5]+' '+ year +' '+r[5:10]
			dayDic['out'] 	= r[0:2]+' '+r[2:5]+' '+ year +' '+r[11:16]
		else:
			dayDic['date'] 	= r[0:1]+' '+r[1:4]+' '+ year
			dayDic['in'] 	= r[0:1]+' '+r[1:4]+' '+ year +' '+r[4:9]
			dayDic['out'] 	= r[0:1]+' '+r[1:4]+' '+ year +' '+r[10:15]
			
		data.append(dayDic)
		#print('\n',r,sep='')
	totalDiff = 0
	print('<table style="border: 1px solid black;border-spacing: 5px">')
	print('<tr>')
	print('<th>')
	print('Date')
	print('</th>')
	print('<th>')
	print('Working Hours')
	print('</th>')
	print('</th>')
	print('<th>')
	print('Diffrence')
	print('</th>')
	print('</tr>')
	for row in data:
		print('<tr style="text-align:center;border: 1px solid black;border-collapse: collapse;">')
		intime = datetime.strptime(row['in'],'%d %b %Y %H:%M')
		outtime = datetime.strptime(row['out'],'%d %b %Y %H:%M')
		working = outtime-intime
		#print(intime)
		#print(outtime)
		workingmin = working.seconds/60
		workingHours = str(int(workingmin//60)).zfill(2)+ ':' +str(int(workingmin%60)).zfill(2)
		
		difference = workingmin - (9*60)
		totalDiff = totalDiff + difference
		prefix = "+" if difference > 0 else " "
		difference = prefix + str(int(difference//60)).zfill(2)+ ':' +str(int(difference%60)).zfill(2)
		#workingHours = int(workingmin%60)
		print('<td>')
		print(datetime.strptime(row['date'],'%d %b %Y').strftime('%d %b %Y'))
		print('</td>')
		
		print('<td>')
		print(workingHours)
		print('</td>')
		
		print('<td>')
		print(difference)
		print('</td>')
		#print(workingHours)
		#print(difference)
		print('</tr>')
	print('</table>')

	prefix = "+" if totalDiff > 0 else ""
	totalDiff = prefix + str(int(totalDiff//60)).zfill(2)+ ':' +str(int(totalDiff%60)).zfill(2)
	print('Total Diff: ')
	print(totalDiff)
except:
  print("An exception occurred")
  

#print(text2)

#print(text)