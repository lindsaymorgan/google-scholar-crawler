#!/usr/bin/env python2

import pickle

from Spider import Spider

def main():
    ### The start page's URL
    start_url = 'https://scholar.google.com.tw/citations?view_op=search_authors&hl=en&mauthors=label:complex_systems'

    ### p_key and n
    p_key = []
    n_key = []

    ### Google Scholar Crawler, Class Spider
    myCrawler = Spider(start_url, p_key, n_key, page=5)

    results = myCrawler.crawl()

    with open('result.pickle', 'wb') as f:
        pickle.dump(results, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
