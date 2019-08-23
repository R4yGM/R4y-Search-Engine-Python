#https://www.googleapis.com/customsearch/v1?key=AIzaSyBFxFPELb5R6rg8iUOBfKYgixfSDNqOG9s&page&cx=017576662512468239146:omuauf_lfve&q=TOSEARCH
import sys
sys.path.insert(1, 'plug/')
from progress_bar import ProgressBar
import time
from time import sleep
from googleapiclient.discovery import build
import json


#def Request#aggiungo qua il loading
global search_word

def Initialize(API_KEY):
    service = build("customsearch", "v1",
            developerKey=API_KEY)

    return service

def Search(a):
    pageLimit = 1000000
    service = Initialize("AIzaSyBFxFPELb5R6rg8iUOBfKYgixfSDNqOG9s")
    startIndex = 1
    response = []

    for nPage in range(0, pageLimit):
        print("--------------------------------------------")
        print ("Reading page number:",nPage+1)
        
        response.append(service.cse().list(
            q=a, 
            cx='001132580745589424302:jbscnf14_dw',  
            lr='lang_en', 
            start=startIndex
        ).execute())
        resp = json.dumps(response)
        print(response[nPage].get("searchInformation").get("totalResults"))
        total_Results = response[nPage].get("searchInformation").get("totalResults")
        if total_Results == "0" :
            print("No results found for: ",a)
            __main__("Restarted")
            
        print(nPage+1)
        print("Total time :",response[nPage].get("searchInformation").get("searchTime"))
        #print("Total time :"+response[nPage].get("searchInformation").get("searchTime"))
        #print("Total time: "+resp['searchInformation']['searchTime'])
        #print("Total results: "+resp[nPage]["searchInformation"]["formattedTotalResults"])
        print("Results: ")
        #items = response[nPage].items
        ab = 0
        for i in response[nPage].get("items") :           
            print(response[nPage]["items"][ab]["title"])
            print(response[nPage]["items"][ab]["link"])
            ab = ab + 1
        print("Page : ",nPage+1)
        #startIndex = response[nPage].get("queries").get("nextPage")[0].get("startIndex")
        print("--------------------------------------------")
        with open('data.json', 'w') as outfile:
            json.dump(response, outfile)
        print("[i] - to search again \n[p] - next page")
        aaaa = input()
        if aaaa == "i" :
            __main__("Started new Search")
        elif aaaa == "p" :
            nPage = nPage + 1
        elif aaaa != "p" :
            print("Unknown command")
            __main__("Restarted")
            

def __main__(stat):
    engine_NM = "R4y-Search: "
    print(engine_NM+stat)
    print("Commands : \n[a] - start search\n[c] - quit")
    e = input()
    if e == "a":
        search = input("\nEnter here ")
        search_word = search
        print("Finding results for :"+search)
        progress = ProgressBar(20, fmt=ProgressBar.FULL)
        for x in range(progress.total):
            progress.current += 1
            progress()
            sleep(0.01)
        progress.done()
        Search(search)
    elif e == "c":
        print("Bye!")
        sys.exit(0)
    
    

if __name__ == "__main__" :
    __main__("Started")
