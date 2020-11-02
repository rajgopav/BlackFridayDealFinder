'''
This will be the main file that will serve as a way to search through all the
websites based on the search input that the user gives.
'''
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from product import Product
import pandas as pd

class DealFinder:
    '''
    This class will go through and find all the deals for the items that the user
    inputs then it will find the top deals that the user wants to see and return
    that data as a csv file
    '''
    search=[]#this will hold the serch terms
    product=[]#this will hold a list of the products found through the websites
    numDeals=0#This will hold the number of top deals that user wants to see
    topDeals=[]#this will hold the top deals

    def __init__(self,searchList,numDeals=15):
        self.search=searchList
        self.numDeals=numDeals#Will default to the top 15 deals




    #TODO: Method to get the top searches
    '''
    We have two possible options: Either to find the max through a linear search,
    or to sort the list and take out the number we want from the top. Given the scope
    of this script, the most resource effecient method would be to simply search
    the list the number of times we want. Even if we used mergesort or quicksort,
    O(nlogn), we would not do better than a simple linear search. The point where
    a sorting algorithm would be more effective is at a point much greater than
    what this script is aming to solve.
    '''

    '''
    Now we will present the functions that will find the products from websites
    '''
    #This will find the deals on amazon
    def findonAmazon(self,itemName):
        "Base Url:https://www.amazon.com/s?k=nintendo+switch+games&page=2&qid=1604344724&ref=sr_pg_2"
        item=''
        words=itemName.split()
        for i in range(0,len(words)):
            #this will split the item's name by the number of words
            if i==0:
                item = item + "{}".format(words[i])
            else:
                #we are at the end
                item = item + "+{}".format(words[i])
        
        baseUrl="https://www.amazon.com/s?k={}&page={}&qid=1604344724&ref=sr_pg_2".format(item,1)
















if __name__ == '__main__':
    list=['Nintendo Switch']
    s=DealFinder(list,10)
    s.findonAmazon(list[0])
