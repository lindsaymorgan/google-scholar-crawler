# google-scholar-crawler

> Crawl [Google Scholar Search Page](https://scholar.google.com.hk) professors of a specific label and sort by number of citations, get information of the email address/personal website/number of citations, and output csv
>


## Get Started

>Need to use requests, BeautifulSoup, pdfkit
>
>Before installing pdfkit, you need to download [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)

## How to Use

### 1. Enter crawlprofessorlist.py

Change the label (Row 18) to search for the professor corresponding to the label

### 2. By setting page = number, you can set the Google Search Page to be crawled

![](https://github.com/linhung0319/google-scholar-crawler/blob/master/set.png)

Setting too many pages will induce Google’s robot check

### 3. Start runing program

Execute crawlprofessorlist.py in Terminal

```
$ python3 google_crawler.py
```

The captured data ('professor name','university','citation number',...) will be stored in result.pickle

Then, execute csvNdownload.py in Terminal

```
$ python3 csvNdownload.py
```

Save data in CSV
