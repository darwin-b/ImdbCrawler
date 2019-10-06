
import requests
import scrapy
import bs4
import re
import webbrowser
from bs4 import BeautifulSoup
from googlesearch import search
import socket

def get_episodes_list(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html5lib')
    # print(soup) 
    refined_div = soup.find_all('div', class_="col-title")  
    flag = False
    episode_dict = {}
    for each in refined_div:
        flag = False
        for href in each.find_all('a'):
            if flag:
                episode_dict[href.get("href")] = href.text
            flag = True
    return episode_dict



# get_imdb_tittle(url)



def get_episode_details(episode_url):
    page = requests.get(episode_url)
    soup = BeautifulSoup(page.text,'html5lib')

    # Extracting Season & Episode Number    
    refined_div = soup.find('div',class_="bp_heading")
    episode_number = refined_div.get_text()

    # Extracting StoryLine
    refined_div = soup.find('div',class_="inline canwrap")
    storyline = refined_div.get_text().strip()

    # Extracing Episode Rating
    refined_div = soup.find('span', itemprop="ratingValue")
    rating = refined_div.get_text()
    refined_div2 = soup.find('span', itemprop="ratingCount")
    rating = refined_div.get_text()+' |users - '+refined_div2.get_text()

    return episode_number,storyline,rating


 









# page = requests.get("https://www.imdb.com"+title_number)
# soup = BeautifulSoup(page.text,'html5lib')
# refined_div = soup.find_all('div',class_="bp_heading")

# filename = "refined_div.html"
# filecontent = str(refined_div)
# f = open(filename,"w",encoding="utf-8")
# f.write(filecontent)
# f.close()


#  <div class="lister-list" >