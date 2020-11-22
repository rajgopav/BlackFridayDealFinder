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
    def findTopDeals(self):
        #We must find the top deal, then remove it from the list and continue
        for i in range(0,self.numDeals):
            #now we must find the max
            maxDeal=self.products[0]#A starter item
            for deal in self.products:
                if deal > maxDeal:
                    #We want to replace the maxDeal with this better deal
                    maxDeal=deal
            # once we have found the maximum, then we can add it to our top deals list
            self.topDeals.append(maxDeal)
            self.products.remove(maxDeal)#We want to remove it from the list so it doesn't show up again






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
                try:
                    link="https://www.amazon.com{}".format(x.h2.a['href'])
                    title=x.h2.a.span.text
                    prices=x.find_all("span",attrs={"class":"a-offscreen"})
                    if len(prices)==1:
                        c=prices[0].text.split("$")[1].replace(",",'')
                        p=prices[0].text.split("$")[1].replace(",",'')
                    elif len(prices)==0:
                        c=100000000000000000000000000#We just want to get rid of this basically
                        p=100000000000000000000000000
                    else:
                        c=prices[0].text.split("$")[1].replace(",",'')
                        p=prices[1].text.split("$")[1].replace(",",'')
                    self.products.append(Product(title,link,c,p))
                except:
                    pass
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
            try:
                url="https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&cp={}&id=pcat17071&iht=y&keys=keys&ks=960&list=n&sc=Global&st={}&type=page&usc=All%20Categories".format(i,item)
                result=self.saveThePage(url=url)
                #Now we want to save the products
                for x in result.find_all("li",attrs={"class":"sku-item"}):
                    try:
                        title=x.h4.a.text
                        link="https://www.bestbuy.com{}".format(x.h4.a['href'])
                        #p=x.find("div",attr={"class":"pricing-price__savings-regular-price"})
                        #print(p)
                        c=x.find("div",class_="priceView-hero-price priceView-customer-price").span.text.split('$')[1].replace(",",'')
                        p=x.find("div",class_="pricing-price__regular-price").text.split('$')[1].replace(",",'')
                        self.products.append(Product(title,link,c,p))
                    except:
                        pass
            except:
                pass

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
            try:
                for item in result.find_all("div",attrs={"class":"search-result-product-title gridview"}):
                    link=("https://www.walmart.com"+item.a['href'])
                    page=self.saveThePage(link)
                    title=page.h1.text
                    #find the current price
                    c=page.find("span",attrs={"id":"price"}).text.split("$")[1].replace(",",'')
                    p=page.find("div",attrs={"class":"price-old display-inline"}).text.split("$")[1].replace(",",'')
            except:
                pass#We only want to save things if there is a deal
            #now once we know for sure we have all the data we need we can input the data
                self.products.append(Product(title,link,c,p))
        print(len(self.products))

    def clearProductList(self):
        #this will clear the product lists
        self.products=[]
        self.topDeals=[]


    def findAll(self,depth):
        #this is the main method that will find the top deals
        for item in self.search:
            self.findOnBestBuy(item,depth)
            print("Found Deals on Best Buy!")
            print("We have {} deals so far".format(len(self.products)))
            self.findOnWalmart(item,depth)
            print("Found Deals on Walmart!")
            print("We have {} deals so far".format(len(self.products)))
            self.findonAmazon(item,depth)
            print("Found Deals on Amazon")
            print("We have {} deals so far".format(len(self.products)))
            self.findTopDeals()
            #now we need to output a csv using pandas
            itemName=[]
            itemPrice=[]
            itemPriceRed=[]
            itemLink=[]
            for topItem in self.topDeals:
                itemName.append(topItem.getName())
                itemLink.append(topItem.getLink())
                itemPrice.append(topItem.getPrice())
                itemPriceRed.append(topItem.getPriceDropPercentage())
            dict={'Name':itemName,'Price':itemPrice,'Percent Off':itemPriceRed,'Link':itemLink}
            deals=pd.DataFrame(dict)
            filename="TopDeals-{}".format(item)
            deals.to_csv("{}.csv".format(filename))
            self.clearProductList()





























if __name__ == '__main__':
    list=['Monitor']
    s=DealFinder(list,10)
    s.findAll(10)
