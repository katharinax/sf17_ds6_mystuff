#!/home/katharina/anaconda3/bin/python


# In[2]:

# If not running on AWS instance,
# keep this running in the command line:
# ssh -NL 12345:localhost:27017 myaws &
# To kill:
# use ps | grep "ssh -NL" to find jobID, then
# kill [jobID]


# In[3]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import re
import json
from pymongo import MongoClient
import warnings
import logging
import gc

# warnings.filterwarnings("ignore")
# get_ipython().magic('matplotlib inline')


# In[4]:

# settings
st_page, end_page = 1, 90
port_num = 27017
del_all_result = False
genre = r"alternate-history"
api_key = "fqX09wQYnt4aDOJxQoRtkQ"
delay = 0.5
# ua = UserAgent()
cook = {
        'Host': 'www.goodreads.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4',
        'Cookie': 'csid=BAhJIhg0MjQtOTQxNDM0My04MTQ3MTU5BjoGRVQ%3D--3769321063104d2fdca8460feb1d6bc3ccf37973; locale=en; csm-sid=654-1843675-5161952; u=LNqZ0RiQEdr8wQDbVI-0pFIBJyV-d6x0bFoID-Zv1lYNS4LK; p=FWSM7ysoJqrQRyJKlPMebjpUWZgP0mmSiQFa4lIefiy5mWRs; _session_id2=95a8c537cdfc330d0d67489207d2fb4e',
        'If-None-Match': 'W/"656e01f96c055e677f1eb0f548dc54d4"'}
log_fn = r"goodreads_data" + str(st_page) + r"_" + str(end_page) + r".log"
logging.basicConfig(filename = log_fn, level = logging.INFO, format = "%(asctime)s %(levelname)s %(message)s")
logging.info("settings" + " port_num " + str(port_num) + " st_page " + str(st_page) +  " end_page " + str(end_page) + " del_all_result " + str(del_all_result))


# In[5]:

def get_bookids(st_page, end_page):
    try:
        book_li = []
        for current_page in range(st_page, end_page + 1):
            logging.info("current_page " + str(current_page))
            # user_agent = {'User-agent': ua.random}
            url = r"https://www.goodreads.com/shelf/show/" + genre + r"?page=" + str(current_page)
            page = requests.get(url, headers = cook)
            soup = BeautifulSoup(page.text, 'lxml')

            book_links = soup.find_all("a", {"class", "bookTitle"})
            for link in book_links:
                bookid = re.sub("\/book\/show\/(?P<bookid>[0-9]+).*", "\g<bookid>", link["href"])
                book_li += [bookid]
            time.sleep(delay + 2 * np.random.rand())
        return book_li
    except Exception as e:
        logging.info("get_bookids() exception: " + str(e))
        pass


# In[6]:

def scrape_to_mongo(bookid):
    logging.info("\n==bookid " + str(bookid) + "==\n")
    try:
        # scrape one book
        # user_agent = {'User-agent': ua.random}
        url = r"https://www.goodreads.com/book/show.xml?key=" + api_key + r"&id=" + str(bookid)
        page = requests.get(url, headers = cook)
        soup = BeautifulSoup(page.text, 'lxml')
        one_book_desc = soup.find("description").text
        one_title = soup.find("h1").text
        one_author = soup.find("name").text
        one_page_ct = soup.find_all("num_pages")[1].text
        one_pub_yr = soup.find("publication_year").text
        one_lang = soup.find("language_code").text
        n_text_reviews = soup.find("text_reviews_count").text
        n_ratings = soup.find("ratings_count").text
        avg_rating = soup.find("average_rating").text

        logging.info("Starting to insert into bookColl")
        bookColl.insert_one({"bookid": bookid,
                             "title": one_title,
                             "author": one_author,
                             "page_ct": one_page_ct,
                             "pub_yr": one_pub_yr,
                             "leng": one_lang,
                             "n_text_reviews": n_text_reviews,
                             "n_ratings": n_ratings,
                             "avg_rating": avg_rating,
                             "desc": one_book_desc
                            })
        logging.info("Finished inserting into bookColl")

        iframe = soup.find("iframe")
        url = re.sub(r"DEVELOPER_ID", api_key, iframe['src']) # url to first page of reviews
        page = requests.get(url, headers = cook)
        soup = BeautifulSoup(page.text, 'lxml')

        # get links to review pages
        all_review_links = []
        all_review_links.extend(soup.find_all("link"))
        some_next_pages = soup.find("div", {"class": "gr_pagination"}).find_all("a")
                # urls to next pages of reviews
                # Note: the num of pages are capped around 9
        for review_page in some_next_pages:
            part_url = review_page["href"]
            url = r"https://www.goodreads.com" + part_url
            page = requests.get(url, headers = cook)
            soup = BeautifulSoup(page.text, 'lxml')
            all_review_links.extend(soup.find_all("link"))

        logging.info("Got all_review_links")
        all_review_links = list(set(all_review_links))
        logging.info("Dedupped all_review_links")

        # get reviews
        for link in all_review_links:
            url = link["href"]
            if re.match("https:\/\/www\.goodreads\.com\/review\/show\/.*", url):
                logging.info("beginning to get reviews for " + url)
                page = requests.get(url, headers = cook)
                soup = BeautifulSoup(page.text, 'lxml')
                user_obj = soup.find("span", {"class": "reviewer"})
                one_userid = re.sub(r"\/user\/show\/(?P<userid>[0-9]+)\-.*", r"\g<userid>", user_obj.find("a")["href"])
                one_review_yr = soup.find("span", {"itemprop": "publishDate"}).text
                one_review = soup.find("div", {"class", "reviewText"}).text
                one_like_ct = re.sub("[^0-9]*", "", soup.find("span", {"class": "likesCount"}).text)
                one_rating = soup.find("div", {"class", "rating"}).find("span", {"class", "value-title"})["title"]

                logging.info("Starting to insert into reviewColl")
                reviewColl.insert_one({"bookid": bookid,
                                       "userid": one_userid,
                                       "rating": one_rating,
                                       "review_yr": one_review_yr,
                                       "like_ct": one_like_ct,
                                       "review": one_review})
                logging.info("Finished inserting into reviewColl")
        gc.collect()
        time.sleep(delay + 2 * np.random.rand())
    except Exception as e:
        logging.info("scrape_to_mongo() exception: " + str(e))
        pass


# In[7]:

mongoClient = MongoClient(port = port_num)
bookiddb = mongoClient.bookiddb2
bookidColl = bookiddb.bookidColl

bookdb = mongoClient.bookdb2
bookColl = bookdb.bookColl

reviewdb = mongoClient.reviewdb2
reviewColl = reviewdb.reviewColl


# In[8]:

if del_all_result:
    del_result = bookidColl.delete_many({})
    del_result = bookColl.delete_many({})
    del_result = reviewColl.delete_many({})


# In[9]:

book_li = get_bookids(st_page, end_page)
logging.info("Got all bookids")
book_li = list(set(book_li))
logging.info("Dedupped bookids")

logging.info("Starting to insert into bookidColl")
bookidColl.insert_one({"st_page": st_page,
                       "end_page": end_page,
                       "book_li": book_li})
logging.info("Finished inserting into bookidColl")


# In[10]:

for bookid in book_li:
    scrape_to_mongo(bookid)
logging.info("All inserted to mongo. Script complete.")


# In[ ]:
