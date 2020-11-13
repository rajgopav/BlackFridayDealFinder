# Black Friday Web Scraper

This will be a project that will find the deals with the most discounts across a couple of websites. This will then output a csv file for reference when finding different deals based on what the user searches. 



### The Stores

- Amazon(Complete)
- Best Buy(Complete)
- Target
- Nebraska Furniture Mart
- Walmart(Done, but could use improvement)

## How the top deals are found

The top deals are found by doing a simple linear search for the biggest discount through the entire populated list of products from all websites. Once the max is found, the item is transferred to another list and removed from the main list and the process is repeated until the number of deals the user requested is found.

#### Algorithm design Rationale
We have two possible options: Either to find the max through a linear search,or to sort the list and take out the number we want from the top. Given the scope of this script, the most resource efficient method would be to simply search the list the number of times we want. Even if we used mergesort or quicksort,O(nlgn), we would not do better than a simple linear search. The point where a sorting algorithm would be more effective is at a point much greater than what this script is aiming to solve.
    

## Next Steps

A possible next step would be to create a django website to house and show all of these deals. Walmart could use some work as well as it is really weird with its HTML where some items have different HTML fields making it very difficult to scrape