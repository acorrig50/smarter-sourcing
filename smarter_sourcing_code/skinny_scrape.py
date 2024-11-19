import requests
from bs4 import BeautifulSoup as bs4
import re
import numpy as np


#NOTE: should just remove all requests except for low to high, other requests return inaccureate data and take up too much time/memory
def the_scraping(input_query):
    # start with the URLS and the different versions, the difference in the URLS to note is that the _sop variable changes its number
    # 1. Best match
    best_match_preowned = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + input_query + "&_sop=12&LH_ItemCondition=4"
    best_match_new = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="+ input_query +"&LH_ItemCondition=1000%7C1750&_sop=12"
    # sold URLs
    best_match_sold_preowned = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="+ input_query +"&_sop=12&LH_Sold=1&LH_Complete=1&rt=nc&LH_ItemCondition=3000"
    best_match_sold_new = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="+ input_query +"&_sop=12&LH_Sold=1&LH_Complete=1&rt=nc&LH_ItemCondition=1000%7C1750"

    # 2. Low to high
    low_to_high_preowned = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + input_query + "&_sop=15&rt=nc&LH_ItemCondition=4"
    low_to_high_new = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="+ input_query + "&_sop=15&rt=nc&LH_ItemCondition=3"
    # sold urls
    low_to_high_preowned_sold = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="+ input_query +"&_blrs=recall_filtering&_sop=15&LH_ItemCondition=3000&rt=nc&LH_Sold=1&LH_Complete=1"
    low_to_high_new_sold = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="+ input_query +"&_blrs=recall_filtering&_sop=15&LH_Sold=1&LH_Complete=1&rt=nc&LH_ItemCondition=1000%7C1750"

    # Now we grab the number of items listed for both URL
    # The element is a h1 class
    element_name = 'srp-controls__count-heading'
    # The nested element with the number is a span class
    actual_element = 'BOLD'
    
    #starting the process
    fifth = requests.get(low_to_high_preowned)
    sixth = requests.get(low_to_high_preowned_sold)
    
    seventh = requests.get(low_to_high_new)
    eighth = requests.get(low_to_high_new_sold)
    
    # store the results of each query in a list
    url_storage = [
        fifth, # 4
        sixth, # 5
        seventh, # 6
        eighth # 7
    ]
    text = []
    values = []
    
    # take the text of each search and store it in "text" list
    for i in range(len(url_storage)):
        soup = bs4(url_storage[i].content, 'html.parser')
        golden_goose = soup.find("h1", {'class':'srp-controls__count-heading'})
        text.append(golden_goose.get_text().split(" "))
        values.append(int(text[i][0].replace('+','').replace(",",'')))
    
    print(values)
    
    try:
        low_to_high_preowned_rate = values[1] / values[0]
    except ZeroDivisionError:
        print("The third check had a zero in it")
    
    try:    
        low_to_high_new_rate = values[3] / values[2]
    except ZeroDivisionError:
        print("The fourth check had a zero in it")
    
    
    # store_values =  best_match_preowned_rate, best_match_new_rate, low_to_high_preowned_rate, low_to_high_new_rate
    
    return low_to_high_preowned_rate, low_to_high_new_rate

var = the_scraping("mens pants size extra large")
print("low to high used rate: {}".format(var[0]))
print("low to high new rate: {}".format(var[1]))
