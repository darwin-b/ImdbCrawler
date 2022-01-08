from joblib import Parallel, delayed
import multiprocessing
import itertools
import sys
import timeit
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
    print("Please select valid IMDB link for tv series")
    print("")
    sys.exit()
# top_ratedlist_url="https://www.imdb.com/search/title/?series=tt2085059&view=simple&count=250&sort=user_rating,desc&ref_=tt_eps_rhs_sm"
episodes_list = crawl.get_episodes_list(top_ratedlist_url)

# multiprocessing support
num_cores = multiprocessing.cpu_count()
print("Num Cores available for multiprocessing: ",num_cores)

start_time = timeit.default_timer()
top_list = Parallel(n_jobs=num_cores)(delayed(crawl.get_episode)(title) for title in episodes_list)
end_time1 = timeit.default_timer()

for title,episode in zip(episodes_list,top_list):
    episode.name = episodes_list[title]

top_list.reverse()
for episode in top_list:
    episode.show_details()
end_time2 = timeit.default_timer()

print("")
print("===============================")
print("===============================")
print("Time taken for crawling: ", end_time1 - start_time, " secs")
print("No of cores used : ", num_cores)
print("No of Episodes : ", len(episodes_list))
print("===============================")
print("===============================")
print("")
