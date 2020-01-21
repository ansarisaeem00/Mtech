#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:41:22 2019

@author: saeem
"""

import requests
import time
import json
import xlwt 
  
workbook = xlwt.Workbook()  
  
sheet = workbook.add_sheet("Data.xls") 

while True:

    url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    querystring = {"units":"metric","departure_time":str(int(time.time())),"traffic_model":"best_guess","origins":"ITPL,Bangalore","destinations":"Tin Factory,Bangalore","key":"GetYourKeyHere"}

    headers = {
        'cache-control': "no-cache",
        'postman-token': "something"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    d = json.loads(response.text)
    #print("On", time.strftime("%I:%M:%S"),"time duration is",d['rows'][0]['elements'][0]['duration']['text'], " & traffic time is ",d['rows'][0]['elements'][0]['duration_in_traffic']['text'])
    
    for i  in range(0,100):
        j = 0
        sheet.write(i, j,time.strftime("%I:%M:%S"))
        j = j+1
        sheet.write(i, j,d['rows'][0]['elements'][0]['duration']['text'])
        j = j+1
        sheet.write(i, j,d['rows'][0]['elements'][0]['duration_in_traffic']['text'])
    
    
    workbook.save("sample.xls") 
    
    #print(response.text)