#!/usr/bin/env python2

import pickle
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s - %(message)s')

import requests
from bs4 import BeautifulSoup
import pdfkit
import time

from ParseOut import ParseOutYear, ParseOutTitle, ParseOutContent, ParseOutTag, ParseOutURL
from Spider import Spider

def main():
    ### The start page's URL
    label='network_science'
    start_url = 'https://scholar.google.com.tw/citations?view_op=search_authors&hl=en&mauthors=label:'+label
    __googleScholarURL="http://scholar.google.com.tw"
    page=20

    ### p_key and n
    p_key = []
    n_key = []

    ### Google Scholar Crawler, Class Spider
    page_url=start_url

    while page>=0:
        res = requests.get(page_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        print("You are now in page ", (page), " !!!")

        ### Test if the crawler is blocked by the Google robot check
        page_links = soup.select('div[class="gs_ai_t"]')
        logger = logging.getLogger('crawl')

        page_url = __googleScholarURL + soup.select('button[aria-label="Next"]')[0]['onclick'][17:-1].replace('\\x3d','=').replace('\\x26','&')

        if not page_links:
            logger.info('1.Google robot check might ban you from crawling!!')
            logger.info('2.You might not crawl the page of google scholar')
        else:
            for index,p in enumerate(page_links):
                info = p.findAll(text=True)
                info = [i for i in info if i != ' ']
                del info[2]
                info[2] = info[2][8:]
                labels = ','.join(info[3:])
                href = __googleScholarURL + soup.select('div[class="gs_ai_t"]')[index].findAll('a', href=True)[0][
                    'href']
                personalpage = requests.get(href)
                personsoup = BeautifulSoup(personalpage.text, 'html.parser')
                try:
                    homepage = personsoup.select('div[class="gsc_prf_il"][id="gsc_prf_ivh"]')[0].findAll('a', href=True)[0][
                        'href']
                except:
                    homepage =''
                info = info[:3] + [homepage] + [labels]
                info_str = '\t'.join(info)
                f = open(f"professors-{label}.csv", "a+")
                f.write(info_str)
                f.write('\n')
                f.close()
                time.sleep(4)



        time.sleep(4)
        page-=1


if __name__ == '__main__':
    main()
