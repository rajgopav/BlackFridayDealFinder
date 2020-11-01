



class Product:
    name=''#this will hold the name of the Product
    description=''#this will hold the price of the Product
    pricePrev=0.0#Holds the previous pricePrev
    priceCurr=0.0#holds the current price
    link=""#this will hold the link for the Product
    store=""#this will hold the store

    def __init__(self,name,description,pricePrev,priceCurr,link,store):
        self.description=description
        self.name=name
        self.pricePrev=pricePrev
        self.priceCurr=priceCurr
        self.link=link
        self.store=store

    def getDescription(self):
        return self.description
    def getPriceDrop(self):
        #this will get the price drop of the Product
        return self.pricePrev - self.priceCurr

    def getPriceDropPercentage(self):
        #this will get the price drop as a percentage
        return (self.getPriceDrop)/self.pricePrev *100
    def getName(self):
        return self.name

    def getStore(self):
        #this will get the store
        return self.store
    def getLink(self):
        return self.store
