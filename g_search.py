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

    results_list = [search_result for search_result in result['items']]
    print(results_list)
    results_list.reverse()
    for index,item in enumerate(results_list) :
        title = item["title"]    
        snippet = item["snippet"]
        url = item["htmlFormattedUrl"]
        print("---------------------------------------------")
        print(str(10-index)+".  "+title)
        print(snippet)
        print(url)
        url_list.append(url)
    url_list.reverse()
    return url_list


# for item1 in result['items']:
#     print("key1: "+ str(item1))
#     print("\n")
#     for key2 in item1:
#         print(str(key2) +":  "+ str(item1[key2]))



