#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:53:59 2019

@author: saeem
"""

# importing googlemaps module 
import googlemaps 

# Requires API key 
gmaps = googlemaps.Client(key='AIzaSyD_nfpawIGZldSmSOow_M5d6BVYvqYrzVc') 

# Requires cities name 
my_dist = gmaps.distance_matrix('Delhi','Mumbai')['rows'][0]['elements'][0] 

# Printing the result 
print(my_dist) 
