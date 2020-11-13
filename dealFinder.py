'''
This will be the main file that will serve as a way to search through all the
websites based on the search input that the user gives.
'''
from bs4 import BeautifulSoup as soup
import urllib.request as uReq
from product import Product
import pandas as pd
import time

class DealFinder:
    '''
    This class will go through and find all the deals for the items that the user
    inputs then it will find the top deals that the user wants to see and return
    that data as a csv file
    '''
    search=[]#this will hold the serch terms
    products=[]#this will hold a list of the products found through the websites
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

        for i in range(1,depth+1):
            url="https://www.amazon.com/s?k={}&page={}&qid=1604344724&ref=sr_pg_{}".format(item,i,i)
            #with this url we can go through and get all the products on the page
            result=self.saveThePage(url)#this will create a soup object we can interface with
            for x in result.find_all("div",attrs={'class':'s-include-content-margin s-border-bottom s-latency-cf-section'}):
                link="https://www.amazon.com{}".format(x.h2.a['href'])
                title=x.h2.a.span.text
                prices=x.find_all("span",attrs={"class":"a-offscreen"})
                if len(prices)==1:
                    c=prices[0]
                    p=prices[0]
                elif len(prices)==0:
                    c=100000000000000000000000000#We just want to get rid of this basically
                    p=100000000000000000000000000
                else:
                    c=prices[0]
                    p=prices[1]
                self.products.append(Product(title,link,c,p))
    def findOnBestBuy(self,itemName,depth=11):
        #Correctly search the item
        item=''
        words=itemName.split()
        for i in range(0,len(words)):
            #this will split the item's name by the number of words
            if i==0:
                item = item + "{}".format(words[i])
            else:
                #we are at the end
                item = item + "%20{}".format(words[i])
        for i in range(0,depth):
            url="https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&cp={}&id=pcat17071&iht=y&keys=keys&ks=960&list=n&sc=Global&st={}&type=page&usc=All%20Categories".format(i,item)
            result=self.saveThePage(url=url)
            #Now we want to save the products
            for x in result.find_all("li",attrs={"class":"sku-item"}):
                title=x.h4.a.text
                link="https://www.bestbuy.com{}".format(x.h4.a['href'])
                #p=x.find("div",attr={"class":"pricing-price__savings-regular-price"})
                #print(p)
                c=x.find("div",class_="priceView-hero-price priceView-customer-price").span.text
                p=x.find("div",class_="pricing-price__regular-price").text.split()[1]
                self.products.append(Product(title,link,c,p))
    def findOnWalmart(self,itemName,depth=11):
        #This will find deals on Nebraska furniture mart

        #Correctly search the item
        item=''
        words=itemName.split()
        for i in range(0,len(words)):
            #this will split the item's name by the number of words
            if i==0:
                item = item + "{}".format(words[i])
            else:
                #we are at the end
                item = item + "+{}".format(words[i])
        for i in range(1,depth):
            url="https://www.walmart.com/search/?page={}&ps=40&query={}".format(i,item)
            try:
                result = self.saveThePage(url).find('div',attrs={'class':"search-product-result"})
            except:
                pass#Walmart seems to be a little weird with their html
            #Now we want to find all the products on the page
            links=[]
            titles=[]
            currentPrices=[]
            previousPrices=[]
            for item in result.find_all("div",attrs={"class":"search-result-product-title gridview"}):
                try:
                    link=("https://www.walmart.com"+item.a['href'])
                    page=self.saveThePage(link)
                    title=page.h1.text
                    #find the current price
                    c=page.find("span",attrs={"id":"price"}).text.split("$")[1]
                    p=page.find("div",attrs={"class":"price-old display-inline"}).text.split("$")[1]
                except:
                    pass#We only want to save things if there is a deal
                #now once we know for sure we have all the data we need we can input the data
                self.products.append(Product(title,link,c,p))
        print(len(self.products))




























if __name__ == '__main__':
    list=['noise cancelling headphones']
    s=DealFinder(list,10)
    s.findOnWalmart(list[0],5)
