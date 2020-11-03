



class Product:
    name=''#this will hold the name of the Product
    pricePrev=0.0#Holds the previous pricePrev
    priceCurr=0.0#holds the current price
    link=""#this will hold the link for the Product

    def __init__(self,name,pricePrev,priceCurr,link):
        self.name=name
        self.pricePrev=pricePrev
        self.priceCurr=priceCurr
        self.link=link


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
