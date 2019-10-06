import requests
import scrapy
import bs4
import re
import webbrowser
from googlesearch import search

from bs4 import BeautifulSoup

import g_search
import Episode
import crawl



search_word = input("Enter your Search Word:   ")
url_list = g_search.google_search(search_word)

print("\n")
choice = input("-----------------------Select your Choice---------------------------\n")
choice = int(choice)
url = url_list[choice-1]
# print(url)

for each in url.split("/"):
    if each=='':
        continue
    if each[0]=='t' and each[1]=='t'and len(each)==9:
        title_number = each

print("-------------------Please wait while we load data-----------------------")
print("------------------------------------------------------------------------")
top_ratedlist_url = "https://www.imdb.com/search/title/?series="+title_number+"&view=simple&count=250&sort=user_rating,desc&ref_=tt_eps_rhs_sm"
# top_ratedlist_url="https://www.imdb.com/search/title/?series=tt2085059&view=simple&count=250&sort=user_rating,desc&ref_=tt_eps_rhs_sm"
episodes_list = crawl.get_episodes_list(top_ratedlist_url)

top_list = []

for title in episodes_list:
    imdb_title_number = title
    episode_url = "https://www.imdb.com" + title
    name = episodes_list[title]
    number, storyline, rating  = crawl.get_episode_details(episode_url) 

    episode_object = Episode.Episode(episode_url,name,number,rating,storyline,imdb_title_number)
    
    top_list.append(episode_object)

for episode in top_list:
    episode.show_details()






