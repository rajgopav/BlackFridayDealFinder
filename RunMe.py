from dealFinder import DealFinder
print("Welcome to the Black Friday Deal Finder")
print("Please enter the items you would like to search")
print("Enter 'done' when you are done with your list")
items=[]
item=""
while item.lower() != 'done':
    item=input("Enter your item:\n")
    if(item.lower() != 'done'):
        items.append(item)
    print("Here are your list so far: \n{}".format(items))
print("\n")
print("Here is your list:\n {}\n If you would like to modify your list, please restart the script".format(items))
depth=int(input("How many pages deep would you like to search?\n"))
print("\n")
numDeals=int(input("How many deals would you like to see?\n"))
deal=DealFinder(items,depth)
deal.findAll(depth)
