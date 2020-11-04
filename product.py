



class Product:
    name=''#this will hold the name of the Product
    pricePrev=0.0#Holds the previous pricePrev
    priceCurr=0.0#holds the current price
    link=""#this will hold the link for the Product

    def __init__(self,name,link,c,p):
        self.name=name
        self.link=link
        self.priceCurr=c
        self.pricePrev=p

    def setPricePrev(self,price):
        self.pricePrev=price
    def setPriceCurr(self,price):
        self.priceCurr=price


    def getPriceDrop(self):
        #this will get the price drop of the Product
        return self.pricePrev - self.priceCurr

    def getPriceDropPercentage(self):
        #this will get the price drop as a percentage
        return (self.getPriceDrop)/self.pricePrev *100
    def getName(self):
        return self.name

    def getLink(self):
        return self.store
