#!C:/Users/kuldeepsingh/AppData/Local/Programs/Python/Python37-32/python3.exe
print("Content-Type: text/text")
print()
import cgitb
import time
cgitb.enable()

import sys
import os
import urllib.request
import json
import requests
import urllib
# Complete the function below.
# https://jsonmock.hackerrank.com/api/countries/search?name=
'''def getMovieTitles(substr):
    titles = []  
    data = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title={}".format(substr))  
    response = json.loads(data.content.decode('utf-8'))    
    for page in range(0, response["total_pages"]):       
        page_response = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title={}&amp;page={}".format(substr, page + 1))    
        page_content = json.loads(page_response.content.decode('utf-8'))
        #print ('page_content', page_content, 'type(page_content)', type(page_content))    
        for item in range(0, len(page_content["data"])):           
             titles.append(str(page_content["data"][item]["Title"]))  
    titles.sort()  
    return titles

print(getMovieTitles("spiderman"))'''

'''
def getCountries(s, p):
		data = requests.get("https://jsonmock.hackerrank.com/api/countries/search?name={}".format(s))  
		response = json.loads(data.text.encode('utf-8'))  
		#URL="https://jsonmock.hackerrank.com/api/countries/search"
		#PARAMS={"name":s}
		#cResponse=requests.get(url = "https://jsonmock.hackerrank.com/api/countries/search?name=un")
		
		print(response)
		
		
		
 
res = getCountries('un', 1)

'''

class Grandparent(object):
    def my_method(self):
        print("Grandparent")

class Parent():
    def my_method(self):
        print("Parent")

class Child(Parent,Grandparent):
    def my_method(self):
        print("Hello Grandparent")
        super(Parent,self).my_method()

c=Child()
c.my_method()