from googlesearch import search
from googleapiclient.discovery import build
import json


# num = 10 load as sets of 10 results per page.
# def gsearch(search_word):
#     for link in search(search_word,tld="co.in",num=10,stop=5,pause=2):
#         print(link)


my_cse_id = "007074868542253045069:8fjm0qbl6qd"
my_api_key = "AIzaSyDYGYwBBvGpRdAVSaQk9iDqusZdjKTZO8A"

url_list =[]
def google_search(search_term, **kwargs):
    service = build("customsearch", "v1", developerKey=my_api_key)
    result = service.cse().list(q=search_term, cx=my_cse_id, **kwargs).execute()
    i=0
    for item in result['items']:
        title = item["title"]    
        snippet = item["snippet"]
        url = item["htmlFormattedUrl"]
        i=i+1
        print("---------------------------------------------")
        print(str(i)+".  "+title)
        print(snippet)
        print(url)
        url_list.append(url)
    return url_list


# for item1 in result['items']:
#     print("key1: "+ str(item1))
#     print("\n")
#     for key2 in item1:
#         print(str(key2) +":  "+ str(item1[key2]))



