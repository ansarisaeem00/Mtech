#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:07:27 2019

@author: saeem
"""

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def printHeap(self):
        print("Heap is : " + str(self.heapList[1:]))
        print("Degree is : " + str(self.currentSize))
    
    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def delMax(self):
      mx = self.heapList.index(max(self.heapList))
      self.heapList.pop(mx)
      self.currentSize = self.currentSize - 1  

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

bh = BinHeap()

while(True):
    	print("\n")
    	print("1.Build Heap")   
    	print("2.Insert node in Heap")
    	print("3.Print Heap")
    	print("4.Delete minimum")
    	print("5.Delete maximum")        
    	print("6.Quit")
    	print("\n")
    	choice = input("Enter your choice")
    	if(choice == "6"):
    		break
    	elif(choice == "2"):
    		data = int(input ("enter node to be insert"))
    		bh.insert(data)
    		
    	elif(choice == "1"):
            data =input ("enter nodes to build heap").split(",")
            arr = [int(num) for num in data]
            bh.buildHeap(arr)
    		    	
    	elif(choice == "3"):
    		bh.printHeap()

    	elif(choice == "4"):
    		bh.delMin()
            
    	elif(choice == "5"):
    		bh.delMax()
    	else:
    		print("Invalid choice, Please select a valid input choice")
            


#bh.buildHeap([17, 9, 5, 2, 3,6,33])

#bh.printHeap()

#bh.insert(33)

#bh.printHeap()

#bh.insert(17)
#bh.printHeap()

#bh.insert(4)
#bh.printHeap()

#print(bh.minChild())
#print(bh.delMin())
#print(bh.delMin())
#print(bh.delMin())
#print(bh.delMin())
