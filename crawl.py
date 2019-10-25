import requests
from bs4 import BeautifulSoup

import Episode

#making dictionary of all episodes and title number
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


# url1 = "https://www.imdb.com/search/title/?series=tt6473300&view=simple&count=250&sort=user_rating,desc&ref_=tt_eps_rhs_sm"
# dic = get_episodes_list(url1)
# print(dic)
# for each in dic:
#     print(dic[each])


def get_episode(title):
    imdb_title_number = title
    episode_url = "https://www.imdb.com" + title
    name = ''

    page = requests.get(episode_url)
    soup = BeautifulSoup(page.text,'html5lib')
    try:
        # Extracting Season & Episode Number    
        refined_div = soup.find('div',class_="bp_heading")
        episode_number = refined_div.get_text()

        # Extracting StoryLine
        refined_div = soup.find('div',class_="inline canwrap")
        # print(refined_div)
        storyline = refined_div.get_text().strip()

        # Extracing Episode Rating
        refined_div = soup.find('span', itemprop="ratingValue")
        rating = refined_div.get_text()
        refined_div2 = soup.find('span', itemprop="ratingCount")
        rating = refined_div.get_text()+' |users - '+refined_div2.get_text()
        # print("----------------\n")
        # print(episode_url,name,episode_number,rating,storyline,imdb_title_number)
        # print("----------------\n")

    except:
        storyline='Details Not Available'
        rating='Rating: Not Applicable'
    episode_object = Episode.Episode(episode_url,name,episode_number,rating,storyline,imdb_title_number)
    return episode_object

# url = "https://www.imdb.com/title/tt10339542/?ref_=adv_li_tt"
# get_episode_details(url)

 


# page = requests.get("https://www.imdb.com"+title_number)
# soup = BeautifulSoup(page.text,'html5lib')
# refined_div = soup.find_all('div',class_="bp_heading")

# filename = "refined_div.html"
# filecontent = str(refined_div)
# f = open(filename,"w",encoding="utf-8")
# f.write(filecontent)
# f.close()


#  <div class="lister-list" >