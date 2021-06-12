from joblib import Parallel, delayed
import multiprocessing
import itertools
import sys

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

try:
    top_ratedlist_url = "https://www.imdb.com/search/title/?series="+title_number+"&view=simple&count=250&sort=user_rating,desc&ref_=tt_eps_rhs_sm"
except:
    print("selected ivalid IMDB link for tv series")
    sys.exit()
# top_ratedlist_url="https://www.imdb.com/search/title/?series=tt2085059&view=simple&count=250&sort=user_rating,desc&ref_=tt_eps_rhs_sm"
episodes_list = crawl.get_episodes_list(top_ratedlist_url)


# print(episodes_list)

# multiprocessing support
num_cores = multiprocessing.cpu_count()
top_list = Parallel(n_jobs=num_cores)(delayed(crawl.get_episode)(title) for title in episodes_list)

for title,episode in zip(episodes_list,top_list):
    episode.name = episodes_list[title]

top_list.reverse()
for episode in top_list:
    episode.show_details()

print("================================================")





