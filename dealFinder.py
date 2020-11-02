'''
This will be the main file that will serve as a way to search through all the
websites based on the search input that the user gives.
'''
from bs4 import BeautifulSoup as soup
import urllib.request as uReq
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
    depth=[]#the number of pages deep the script should go

    def __init__(self,searchList,numDeals=15):
        self.search=searchList
        self.numDeals=numDeals#Will default to the top 15 deals

    #A method that will open pages with bs4
    def saveThePage(self,url):
        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
        req = uReq.Request(url, headers=hdr)
        response = uReq.urlopen(req)
        content= response.read()
        response.close()
        return soup(content,'html.parser')





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
    def findonAmazon(self,itemName,depth=11):
        item=''
        words=itemName.split()
        for i in range(0,len(words)):
            #this will split the item's name by the number of words
            if i==0:
                item = item + "{}".format(words[i])
            else:
                #we are at the end
                item = item + "+{}".format(words[i])

        products=[]#will hold the links to the product pages
        for i in range(1,depth+1):
            url="https://www.amazon.com/s?k={}&page={}&qid=1604344724&ref=sr_pg_{}".format(item,i,i)
            #with this url we can go through and get all the products on the page
            result=self.saveThePage(url)#this will create a soup object we can interface with
            for x in result.find_all("h2",attrs={'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}):
                products.append(x.a['href'])
        





        #products.append(self.saveThePage(pUrl))



















if __name__ == '__main__':
    list=['Nintendo Switch']
    s=DealFinder(list,10)
    s.findonAmazon(list[0],2)
